# Internal Sources Research: Anki Programmatic Management API

## Executive Summary

Amazon internal wikis document extensive use of AnkiConnect + Obsidian toolchains for programmatic flashcard management. Key patterns found include: REST API wrappers over AnkiConnect, SQLite WAL mode for concurrency, cross-platform file locking for local data stores, and FastAPI localhost-binding patterns for local HTTP services.

---

## 1. AnkiConnect Addon — REST API Architecture

**Source:** [PkmsToolchain Wiki](https://w.amazon.com/bin/view/PkmsToolchain/) (owner: haziq-only)

### How It Works
- **AnkiConnect** (addon ID: `2055492159`) is an Anki plugin that starts a **local HTTP server** providing a REST API into Anki
- Default port: **8765** on localhost
- Provides full CRUD operations on decks, notes, cards
- Used in combination with **Obsidian_to_Anki** plugin (github.com/Pseudonium/Obsidian_to_Anki)

### Key Architecture Insight
The Obsidian_to_Anki plugin demonstrates the **update-without-duplicate pattern**:
- You write Q/A blocks in markdown notes
- When you hit sync, it **automatically generates OR updates** the corresponding Anki flashcard
- It maintains a bidirectional connection between source note and Anki card
- Single source of truth (markdown) drives the flashcard state

### Capabilities Confirmed
- Create/update/delete notes and decks
- Find notes by query (deck, tags, field content)
- Add media files
- Get/set card scheduling info
- Batch operations (multi action)

### Limitations (from wiki context)
- **Requires Anki desktop running** — the REST server only exists when Anki app is open
- AGPL-3.0 license concern noted (prohibited in Amazon corporate context per policy.amazon.com/standard/82477 — but fine for personal use)
- No built-in authentication (localhost-only by default)

---

## 2. SQLite Concurrency & File Locking Patterns

### 2.1 SQLite WAL Mode for Concurrent Access

**Source:** [Temporalis Microservice Migration](https://w.amazon.com/bin/view/Temporalis/features/distributed-service/deployment/microservice-migration/scope/)

Key finding from the Temporalis team's risk analysis:

| Risk | Impact | Mitigation |
|------|--------|------------|
| SQLite concurrency | DRR orchestrator + DP workers write concurrently to SQLite | **Use WAL mode**; SQLite handles concurrent reads well; writes are serialized but DRR write volume is low |

**Applicability to Anki:** Anki's collection.anki2 is a SQLite database. If multiple agents try to write simultaneously:
- Enable WAL mode (`PRAGMA journal_mode=WAL`)
- Concurrent reads are safe
- Writes are serialized (one writer at a time)
- For low write volume (typical for flashcard updates), this is sufficient

### 2.2 Cross-Platform File Locking

**Source:** [Kiro Memory MCP](https://w.amazon.com/bin/view/Users/sandykol/Automations/KiroMemoryMcp/)

Production-proven pattern for cross-platform file locking in Python:

```python
from contextlib import contextmanager
import sys

if sys.platform == "win32":
    import msvcrt
else:
    import fcntl

LOCK_FILE = MEMORY_DIR / ".patterns.lock"

@contextmanager
def file_lock():
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    lock = open(LOCK_FILE, "w")
    try:
        if sys.platform == "win32":
            msvcrt.locking(lock.fileno(), msvcrt.LK_LOCK, 1)
        else:
            fcntl.flock(lock, fcntl.LOCK_EX)
        yield
    finally:
        try:
            if sys.platform == "win32":
                msvcrt.locking(lock.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(lock, fcntl.LOCK_UN)
        finally:
            lock.close()
```

**Key design decisions from this source:**
- Nested try/finally guarantees lock release even if unlock raises
- JSONL chosen over SQLite for simplicity: "human-readable, git-diffable, append-friendly, no binary dependencies"
- All read-modify-write operations wrapped in the lock context manager

### 2.3 Kamino MetaData Manager — Three-Tier SQLite Caching

**Source:** [Kamino MetaData Manager & SQLite Infrastructure](https://w.amazon.com/bin/view/AWS/DMS/AWS_Database_Migration_Service/Documentation/Kamino/Training/MetaDataManagerAndSQLiteInfrastructure/)

Relevant architecture pattern:
```
Tier 1: Memory → Hash tables (microseconds)
   ↓ miss
Tier 2: SQLite → on disk (milliseconds)
   ↓ miss
Tier 3: Backend DB → Live query (seconds)
```

**Concurrency model uses six locks** for different SQLite files. Relevant for Anki if we need to manage both the collection and media separately.

---

## 3. Local HTTP API Service Patterns

### 3.1 FastAPI Bridge Pattern

**Source:** [Useful API Patterns Wiki](https://w.amazon.com/bin/view/Users/swinyted/useful-api-patterns/)

Key pattern documented: **"FastAPI bridge for native apps via local REST API"**
- Avoids rewriting complex logic in another language
- Thin REST layer over existing Python functionality
- Shared batch file / Makefile integration for starting the service

### 3.2 Localhost Security (MANDATORY for local services)

**Source:** [AIOps Team Security Runbook](https://w.amazon.com/bin/view/AmazonWebServices/SalesSupport/DeveloperSupport/AWSSupport-AIOps/Runbooks/Development-Best-Practices/)

Security best practices for local HTTP services:

**FastAPI / Uvicorn binding:**
```python
uvicorn.run(app, host="127.0.0.1", port=PORT)
```

**Flask binding:**
```python
app.run(host="127.0.0.1", port=PORT)
```

**Defense-in-Depth: LocalhostOnlyMiddleware (MANDATORY for FastAPI/Starlette)**

**CORS Restriction (MANDATORY):**
- Only allow origins from localhost

### 3.3 FastAPI vs Flask for Local Services

**Source:** [IhmSDP FastAPI ASGI](https://w.amazon.com/bin/view/IhmSDP/FastAPIASGI/)

| Framework | Async | Performance | Use Case |
|-----------|-------|-------------|----------|
| Flask | WSGI (sync) | Lower | Simple, synchronous operations |
| FastAPI | ASGI (async) | Higher | Concurrent requests, better for proxy pattern |

**Recommendation for Anki wrapper:** FastAPI is preferred because:
- Async support means the API can handle multiple incoming requests while waiting for AnkiConnect responses
- Better request validation with Pydantic models
- Automatic OpenAPI documentation

---

## 4. Card Identity & GUID Patterns

### 4.1 GUID as Stable Identifier

**Source:** [RISC GDA GUID tracking](https://w.amazon.com/bin/view/RISC_GDA/AWD/sa_amelia_guid/)

General pattern for GUID usage in Amazon systems:
- "Globally Unique Identifier provides precise tracking capabilities across distributed systems"
- "Serves as a stable, permanent reference for correlation, auditing, and data lineage"
- "Enables accurate tracking of data flow through complex multi-system architectures"

**Application to Anki:** The same principle applies — using deterministic GUIDs based on content hash (e.g., `hashlib.sha256(f"{deck}::{front_field}".encode()).hexdigest()[:10]`) enables:
- Idempotent updates (same input → same GUID → update not create)
- Tracking card lineage across regeneration cycles
- Safe re-import without duplicates

### 4.2 Obsidian_to_Anki's Approach to Card Identity

From the PkmsToolchain wiki context, the Obsidian_to_Anki plugin:
- Stores Anki note IDs as metadata in the Obsidian markdown file
- On first sync: creates note, stores returned ID
- On subsequent syncs: uses stored ID to call `updateNoteFields` via AnkiConnect
- If ID is missing/invalid: treats as new note creation

---

## 5. Architecture Options Assessment (Internal Source Perspective)

### Option A: Thin Wrapper over AnkiConnect (RECOMMENDED)

**Evidence from internal sources:**
- PkmsToolchain confirms this is proven and reliable
- FastAPI bridge pattern from swinyted wiki shows how to add queueing/batching
- AIOps runbook provides security guidance for localhost services

**Architecture:**
```
Your Code → FastAPI Local Service (port 5555) → AnkiConnect (port 8765) → Anki Desktop
```

**Pros:** All Anki features available, scheduling preserved, media handling built-in
**Cons:** Requires Anki desktop running

### Option B: Direct SQLite Manipulation (RISKY)

**Evidence from internal sources:**
- Kamino's six-lock model shows SQLite concurrency is solvable but complex
- Temporalis WAL mode mitigates concurrent read issues
- BUT: Anki's SQLite schema is undocumented internal API, prone to breaking changes

**Recommendation:** Only for read operations (analytics, export). Never for writes in production.

### Option C: .apkg Generation + Import via AnkiConnect

**Evidence:**
- genanki referenced in multiple search results (Skylarli wiki, AR GenAI Champions)
- AnkiConnect's `importPackage` action can import .apkg files
- **CONCERN:** May reset scheduling data (needs verification from other agents)

### Option D: Hybrid (BEST for the use case)

Combine:
1. **genanki with deterministic GUIDs** for initial deck generation
2. **AnkiConnect `updateNoteFields`** for incremental updates
3. **FastAPI wrapper** for queueing and error handling
4. **File locking** (fcntl pattern from Kiro Memory) for concurrent agent safety

---

## 6. Media File Handling

**Source:** [Kindle Flashcards Export Design](https://w.amazon.com/bin/view/KindleEducation/Client/Flashcards/FlashcardsExportHighLevelDesign/)

Pattern for media in flashcards:
- Store media files separately (S3 in their case; local `collection.media/` for Anki)
- Reference media by filename in card content: `[sound:filename.mp3]`
- AnkiConnect provides `storeMediaFile` action for programmatic media upload
- Batch upload pattern: iterate files, call storeMediaFile for each

---

## 7. Error Handling & Rollback

**Source:** Temporalis microservice migration risks + Kiro Memory MCP patterns

Recommended approach:
1. **Wrap all operations in file lock** (prevents concurrent corruption)
2. **Use WAL mode** if directly touching SQLite
3. **Backup before bulk operations** (cp collection.anki2 collection.anki2.bak)
4. **Idempotent operations** — design so re-running produces same result
5. **Verify after write** — query AnkiConnect to confirm note exists/updated

---

## 8. Notable Internal Anki Usage

| Wiki Page | Author | Use Case |
|-----------|--------|----------|
| [Skylarli/Anki_Build_Decks](https://w.amazon.com/bin/view/Skylarli/Anki_Build_Decks/) | skylarli | Infrastructure build process flashcards |
| [PkmsToolchain](https://w.amazon.com/bin/view/PkmsToolchain/) | haziq | AWS certification study with Obsidian→Anki sync |
| [ARGenAIChampions](https://w.amazon.com/bin/view/ARGenAIChampions/ARAllTeamsAIUseOct2025/) | cpfschw | LLM-generated Anki cards from paper reading sessions (TSV export) |
| [Users/rawlsimo](https://w.amazon.com/bin/view/Users/rawlsimo/Onboarding/) | rawlsimo | Team onboarding flashcards with photos (media handling) |
| [Users/andkai](https://w.amazon.com/bin/view/Users/andkai/Studying/) | andkai | AWS certification prep referencing Anki |

---

## 9. Key Takeaways for Implementation

1. **AnkiConnect is the proven integration point** — multiple Amazon engineers use it successfully for programmatic updates
2. **Deterministic GUIDs** are the solution to the delete→import cycle — use content-based hashing
3. **FastAPI on localhost** is the recommended pattern for wrapping AnkiConnect with additional logic
4. **File locking with fcntl** is the standard pattern for preventing concurrent corruption
5. **SQLite WAL mode** if touching the database directly (read-only recommended)
6. **Media files** go through `storeMediaFile` API, referenced by filename in HTML
7. **The Obsidian_to_Anki plugin** proves that "update in place" without scheduling loss is achievable via `updateNoteFields`
