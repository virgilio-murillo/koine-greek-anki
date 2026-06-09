# VALIDATION SKIPPED (head agent finalized)

# Local API Service for Programmatic Anki Management — Research Findings

_Agent: c3-context | Date: 2025-06-05 | Source: Local code analysis + web research_

---

## 1. AnkiConnect Addon — API Capabilities

**Source:** https://git.sr.ht/~foosoft/anki-connect/ (official repo, maintained)

### How It Works
- Anki desktop addon (code: `2055492159`) that starts an HTTP server on `localhost:8765`
- JSON-RPC style: POST JSON with `{"action": "...", "version": 6, "params": {...}}`
- Requires Anki desktop to be running in background
- All operations run on Anki's main thread (serialized, safe)

### Key Actions for Deck Management

| Category | Actions |
|----------|---------|
| **Notes (CRUD)** | `addNote`, `addNotes`, `updateNoteFields`, `updateNote`, `updateNoteModel`, `deleteNotes`, `findNotes`, `notesInfo` |
| **Decks** | `createDeck`, `deleteDecks`, `changeDeck`, `deckNames`, `getDeckStats` |
| **Models** | `createModel`, `modelNames`, `updateModelTemplates`, `updateModelStyling` |
| **Media** | `storeMediaFile` (base64/path/URL), `deleteMediaFile`, `getMediaDirPath`, `getMediaFilesNames` |
| **Import/Export** | `importPackage`, `exportPackage` |
| **Batch** | `multi` (execute multiple actions in one request) |
| **Search** | `findNotes` with Anki query syntax, `findCards` |
| **Sync** | `sync` (trigger AnkiWeb sync) |

### Limitations
- **Requires Anki running** — cannot operate headless
- **Single-user** — designed for localhost only (configurable binding)
- **No bulk update** — `updateNoteFields` takes one note ID at a time (use `multi` for batching)
- **No atomic transactions** — partial failures in `addNotes` leave partial state
- **Note ID required for updates** — must `findNotes` first, then update by ID
- **Warning:** Cannot update note fields while viewing that note in Anki browser

### Already In Use in This Project
The project's `koine-anki/terminaciones/deploy.py` already implements:
```python
ANKICONNECT_URL = "http://localhost:8765"
# Uses: version, importPackage, sync
```

---

## 2. Direct .apkg File Manipulation

### .apkg Format
- ZIP archive containing:
  - `collection.anki2` or `collection.anki21` — SQLite database
  - `media` — JSON mapping of numeric filenames to original names
  - `0`, `1`, `2`... — actual media files (renamed to numbers)

### SQLite Schema (collection.anki2)
```sql
CREATE TABLE notes (id, guid, mid, mod, usn, tags, flds, sfld, csum, flags, data);
CREATE TABLE cards (id, nid, did, ord, mod, usn, type, queue, due, ivl, factor, reps, lapses, left, odue, odid, flags, data);
CREATE TABLE revlog (id, cid, usn, ease, ivl, lastIvl, factor, time, type);
CREATE TABLE col (id, crt, mod, scm, ver, dty, usn, ls, conf, models, decks, dconf, tags);
```

Key fields:
- `notes.guid` — globally unique identifier, used for import deduplication
- `notes.flds` — all field values separated by `\x1f` (unit separator)
- `notes.mid` — model/note-type ID
- `cards.did` — deck ID

### Risks of Direct SQLite Access
- **File locking:** Anki holds an exclusive lock while running → SQLITE_BUSY
- **Schema changes:** Anki updates may change schema without notice
- **Integrity:** Must maintain all cross-references (csum, usn, mod timestamps)
- **Sync breakage:** Incorrect `usn` values will cause sync conflicts

---

## 3. Python Libraries Comparison

### genanki (RECOMMENDED for this project)
- **Already in use** throughout `koine-anki/` and `koine-pimsleur/`
- Generates .apkg files programmatically
- Supports stable GUIDs (critical for updates without duplicates)
- Media file embedding via `Package.media_files`
- **Pros:** Simple, well-maintained, no Anki dependency, creates importable packages
- **Cons:** Cannot read existing collections, generation-only

### Official `anki` package (`pip install anki`)
- Can open `collection.anki2` directly for full CRUD
- **Critical limitation:** Cannot be used while Anki desktop is running (same DB lock)
- Contains full backend (Rust compiled extensions)
- Useful for batch operations when Anki is closed
- **Pros:** Full API, official support, correct handling of all internal state
- **Cons:** Heavy dependency, platform-specific binaries, exclusive access only

### AnkiPandas
- Reads collection as pandas DataFrames
- Write support is experimental/limited
- **Pros:** Great for analysis/auditing
- **Cons:** Immature write support, not suitable for production updates

### py-anki (community)
- Deprecated/unmaintained, superseded by official `anki` package

---

## 4. Concurrency Concerns

### The Core Problem
- SQLite allows only ONE writer at a time
- Anki desktop holds the database lock exclusively while running
- Direct DB access while Anki is open → `SQLITE_BUSY` errors

### AnkiConnect Safety Model
- All AnkiConnect requests are dispatched on Anki's **main Qt thread**
- Naturally serialized — no concurrent write conflicts possible
- Multiple agents sending requests simultaneously are safe (queued by Anki)

### Multi-Agent Architecture Recommendations
1. **Single entry point:** All agents funnel through one AnkiConnect endpoint
2. **Request queuing:** If building a wrapper API, implement a request queue
3. **Retry with backoff:** For transient failures (Anki busy with UI operation)
4. **Lock file for .apkg generation:** Multiple processes generating .apkg simultaneously is safe (different files), but importing them must be serialized

---

## 5. Architecture Options Analysis

### Option A: Thin Wrapper over AnkiConnect ⭐ RECOMMENDED

```
[Agent/Script] → [Your HTTP API (FastAPI)] → [AnkiConnect:8765] → [Anki Desktop]
```

**Pros:**
- Safest approach — Anki manages all state
- Already proven in this project (`deploy.py`)
- Full CRUD (findNotes → updateNoteFields)
- Media handling via storeMediaFile
- Sync support built-in

**Cons:**
- Requires Anki desktop running
- Slightly slower (HTTP overhead)
- Limited to AnkiConnect's API surface

**Best for:** Live updates, interactive workflows, CI/CD with Anki open

### Option B: Direct SQLite Manipulation ❌ NOT RECOMMENDED

**Pros:** No Anki needed, fast batch operations
**Cons:** Dangerous (schema changes, sync breakage, file locking), requires Anki to be closed

### Option C: .apkg Generation + AnkiConnect Import (CURRENT APPROACH)

```
[Script] → genanki → .apkg file → AnkiConnect.importPackage() → Anki
```

**Pros:**
- Already working in this project
- Clean separation: generation vs import
- Works with stable GUIDs (overwrites existing notes on reimport)

**Cons:**
- **Import replaces all fields** — cannot update individual fields
- Scheduling data (reviews, intervals) is PRESERVED on reimport with same GUID
- Cannot add/remove individual cards from existing deck without regenerating entire deck

**Best for:** Bulk deck regeneration workflows

### Option D: Hybrid Approach ⭐⭐ BEST FIT FOR THIS PROJECT

```
[Generation scripts] → genanki (with stable GUIDs) → .apkg
[Deploy script] → AnkiConnect.importPackage() for bulk updates
[Fine-grained API] → AnkiConnect.findNotes/updateNoteFields for individual edits
[Media uploads] → AnkiConnect.storeMediaFile for audio files
```

**Rationale for this project:**
- Existing `gen_all_decks.py` + `deploy.py` pattern already works well
- Add AnkiConnect CRUD layer for individual card updates
- Keep genanki for full deck regeneration
- Use storeMediaFile for audio (koine-pimsleur audio cards)

---

## 6. Deck Updates: Modify vs Replace

### With genanki (current .apkg approach)
- **GUID matching is the key:** When importing an .apkg, Anki matches notes by GUID
- If GUID matches → **existing note fields are OVERWRITTEN**
- Scheduling data (reviews, intervals, ease) is **PRESERVED** ✅
- If GUID doesn't match → new note is created (duplicate)

### Current Project's GUID Strategy
Default genanki GUID = `hash(all_fields)`. This means:
- If you change any field → GUID changes → duplicate created ❌
- **Solution:** Custom GUID based on stable identity

```python
class StableNote(genanki.Note):
    @property
    def guid(self):
        # Hash only the identity fields (e.g., deck_id + card_index)
        return genanki.guid_for(self.fields[0])  # or a custom stable key
```

### With AnkiConnect (fine-grained)
```python
# 1. Find existing notes
note_ids = anki_request("findNotes", query='deck:"Koiné Griego" tag:verb_presente')
# 2. Update specific fields
anki_request("updateNoteFields", note={"id": note_ids[0], "fields": {"Back": "new content"}})
```

### Recommended Strategy for This Project
1. **Keep stable Model IDs and Deck IDs** (already documented in CONVENTIONS.md)
2. **Add stable GUIDs** to genanki notes (hash deck_id + card_position or a content key)
3. **Regenerate + reimport** for bulk changes (leveraging GUID matching)
4. **AnkiConnect updateNoteFields** for individual corrections

---

## 7. Media File Handling for Audio Cards

### genanki Approach (for .apkg generation)
```python
my_package = genanki.Package(my_deck)
my_package.media_files = ['audio/word1.mp3', 'audio/word2.mp3']
my_package.write_to_file('output.apkg')
# In note fields: [sound:word1.mp3]
```

### AnkiConnect Approach (for live updates)
```python
# Store file from disk
anki_request("storeMediaFile", filename="greek_word.mp3", path="/absolute/path/to/file.mp3")
# Or from URL
anki_request("storeMediaFile", filename="greek_word.mp3", url="https://...")
# Or from base64
anki_request("storeMediaFile", filename="greek_word.mp3", data="SGVsbG8...")
# Then reference in note field: [sound:greek_word.mp3]
```

### This Project's Audio Pipeline
`koine-pimsleur/src/tts.py` generates audio via:
- Google Cloud TTS (el-GR voices: Chirp3-HD-Achird, Zephyr, Charon, Aoede)
- AWS Polly (fallback for Spanish)
- Cache in `/tmp/tts_cache/`

**Integration path:** Generate audio → `storeMediaFile` → reference `[sound:filename.mp3]` in note fields

---

## 8. Card Identity — Best Practices

### The Duplicate Problem
- Anki identifies notes by GUID (stored in `notes.guid` column)
- Default genanki GUID = hash of ALL fields → changes on any edit → duplicates
- `.apkg` import matching: GUID match → overwrite; no match → new note

### CONVENTIONS.md Already Has Stable IDs
```
| Deck 1: Presente | Model 1847293651 | Deck 1847293652 |
| Deck 2: Imperfecto | Model 1847293653 | Deck 1847293654 |
... (7 decks with hardcoded IDs)
```

### Recommended GUID Strategy
```python
class StableNote(genanki.Note):
    def __init__(self, stable_id, **kwargs):
        self._stable_id = stable_id
        super().__init__(**kwargs)
    
    @property
    def guid(self):
        return genanki.guid_for(self._stable_id)

# Usage: identity = f"{deck_name}:{tense}:{verb}:{ending_idx}"
note = StableNote(
    stable_id="presente:λύω:1sg_act_ind",
    model=model,
    fields=[front_html, back_html]
)
```

### For AnkiConnect Updates
- `findNotes` with query: `"deck:Koiné Griego::Terminaciones" "Front:*λύ*"`
- Store the mapping: `{stable_id: anki_note_id}` locally for fast lookups
- On update: look up note_id → `updateNoteFields`

---

## 9. Error Handling and Rollback

### AnkiConnect Error Patterns
```python
{"result": null, "error": "unsupported action"}           # Wrong action name
{"result": null, "error": "model was not found: X"}       # Model doesn't exist
{"result": null, "error": "cannot create note because it is a duplicate"}
```

### Rollback Strategies

**For .apkg import:**
- `exportPackage` before import → restore point
- Anki has built-in undo (`guiUndo`) for last operation only
- Best: maintain deck generation scripts as source of truth (re-generate to rollback)

**For AnkiConnect CRUD:**
- Read before write: `notesInfo` → save state → modify
- Implement wrapper with transaction log:
```python
class AnkiTransaction:
    def __init__(self):
        self.log = []
    
    def update_note(self, note_id, fields):
        # Save current state
        current = anki_request("notesInfo", notes=[note_id])
        self.log.append(("update", note_id, current["result"][0]["fields"]))
        # Apply change
        anki_request("updateNoteFields", note={"id": note_id, "fields": fields})
    
    def rollback(self):
        for action, note_id, old_fields in reversed(self.log):
            anki_request("updateNoteFields", note={"id": note_id, "fields": old_fields})
```

**For this project specifically:**
- Source of truth = Python generation scripts (not Anki DB)
- Rollback = re-run generation scripts with previous parameters
- Git tracks all card data files → `git checkout` = rollback

---

## 10. Existing MCP Servers for Reference

Multiple AnkiConnect MCP servers exist (all wrap AnkiConnect):
- `CamdenClark/anki-mcp-server` — GitHub, basic CRUD
- `mcp-ankiconnect` (PyPI) — pip installable, Claude integration
- `spacholski1225/anki-connect-mcp` — full featured
- `arielbk/anki-mcp` — deck management + study insights

These could be used directly OR as architecture reference for building a custom local API.

---

## 11. Recommended Architecture for This Project

### Immediate (Low Effort, High Value)
1. **Add stable GUIDs** to `gen_all_decks.py` notes (custom `guid` property)
2. **Enhance `deploy.py`** to support selective deck updates (not just bulk import)
3. **Add `--update-cards` flag** that uses `findNotes` + `updateNoteFields` for individual edits

### Medium Term (Local API Service)
```
┌─────────────────────────────────────────────────┐
│  Local Anki API Service (FastAPI, port 9000)    │
├─────────────────────────────────────────────────┤
│ POST /decks/{name}/regenerate  → genanki → importPackage          │
│ POST /notes/{id}/update        → updateNoteFields                  │
│ POST /notes/search             → findNotes + notesInfo             │
│ POST /media/upload             → storeMediaFile                    │
│ POST /sync                     → sync                              │
│ GET  /decks                    → deckNamesAndIds                   │
│ GET  /health                   → version check                     │
├─────────────────────────────────────────────────┤
│ Queue/retry layer + transaction logging          │
│ Stable GUID registry (JSON file)                 │
└───────────────────┬─────────────────────────────┘
                    │ HTTP
                    ▼
        ┌──────────────────────┐
        │ AnkiConnect :8765    │
        │ (Anki Desktop)       │
        └──────────────────────┘
```

### Key Design Decisions
1. **genanki for generation** (keeps working)
2. **AnkiConnect for import/update** (safe, serialized)
3. **Stable GUID registry** — maps `{deck:card_identity} → anki_note_id` for fast updates
4. **No direct SQLite access** — too risky, breaks sync
5. **Queue for concurrent agents** — serialize requests to avoid race conditions
6. **Transaction log** — enables rollback for batch operations

---

## Summary: Eliminating Delete→Import Cycles

The delete→import cycle exists because:
1. Default GUIDs change when content changes → Anki sees "new" notes
2. No mechanism to update existing notes in-place via .apkg

**Solutions (in order of implementation ease):**

| Solution | Effort | Preserves Reviews? | Granularity |
|----------|--------|-------------------|-------------|
| Stable GUIDs in genanki | Low | ✅ Yes | Entire deck reimport |
| AnkiConnect updateNoteFields | Medium | ✅ Yes | Individual notes |
| Full local API service | High | ✅ Yes | Any operation |

**Quickest win:** Implement custom `guid` property in `gen_all_decks.py` → reimport overwrites existing notes without creating duplicates, preserving all scheduling data.
