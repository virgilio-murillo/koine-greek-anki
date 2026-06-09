# Anki Local API — Investigation Recommendations
_Updated: 2026-06-05T11:05 — HEAD agent synthesis from 5 parallel streams_

---

## Executive Summary

The project **already has the right architecture** (genanki + AnkiConnect `importPackage`). The
current pain point (manual delete→import cycles) has **one root cause**: genanki uses a default
GUID that is a hash of ALL fields. When any field content changes, the GUID changes, so the
re-import creates a **duplicate** instead of updating the existing card.

**Fix: override `guid` in your `Note` subclass** to hash only stable identity fields. Everything
else in the existing pipeline is sound.

The local HTTP API question is answered below with a concrete architecture.

---

## Critical Finding: The Duplicate Root Cause

```python
# CURRENT CODE — WRONG: GUID = hash(all fields) → content change = new GUID = duplicate
deck.add_note(genanki.Note(model=model, fields=[front, back]))

# FIX: GUID = hash(stable identity fields only)
import genanki

class StableNote(genanki.Note):
    """Note whose GUID is derived from stable identity, not content."""
    def __init__(self, *args, identity_key: str, **kwargs):
        super().__init__(*args, **kwargs)
        self._identity_key = identity_key

    @property
    def guid(self):
        return genanki.guid_for(self._identity_key)
```

Usage in `gen_all_decks.py`:
```python
# identity = deck_id + verb_key + form index — never changes even if HTML content is edited
identity = f"{deck_id}:{verb_key}:{form_idx_in_tense}"
deck.add_note(StableNote(model=model, fields=[front, back], identity_key=identity))
```

With stable GUIDs, re-running `deploy.py` will UPDATE existing cards (preserving review history
/ scheduling) instead of creating duplicates. **No delete cycle needed.**

---

## Architecture Options — Decision Matrix

| Option | Description | Requires Anki Running | Risk | Verdict |
|---|---|---|---|---|
| **A** | Thin FastAPI wrapper over AnkiConnect | **Yes** | Low | ✅ Best for automation |
| **B** | Direct SQLite manipulation | No | **High** — SQLITE_BUSY error if Anki is open | ❌ Avoid |
| **C** | genanki + importPackage (current) | Yes (for import) | Low | ✅ Already in use — fix GUIDs |
| **D** | Hybrid: genanki bulk + updateNoteFields for patches | Yes | Low | ✅ Best for incremental |

**Recommendation: Hybrid D** — bulk updates via regenerate+import with stable GUIDs; single-card
patches via `updateNoteFields`.

---

## Recommended Architecture: Local HTTP API

```
┌─────────────────────────────────────────────────────────────────┐
│                     anki-api  (FastAPI, port 9000)              │
│                                                                 │
│  POST /deck/rebuild       →  gen_all_decks.py + importPackage   │
│  PUT  /note/{id}/field    →  updateNoteFields                   │
│  POST /media              →  storeMediaFile (base64)            │
│  GET  /note/find?q=...    →  findNotes → notesInfo              │
│  POST /batch              →  multi (batch AnkiConnect calls)    │
└────────────────────┬────────────────────────────────────────────┘
                     │  JSON-RPC  localhost:8765
           ┌─────────▼──────────┐
           │  AnkiConnect v6    │  (addon inside Anki Desktop)
           └─────────┬──────────┘
                     │  Qt main thread (serialized)
           ┌─────────▼──────────┐
           │  collection.anki2  │  SQLite — ONE writer at a time
           └────────────────────┘
```

**Key constraint**: All writes must go through AnkiConnect (the serialization layer). Never write
directly to `collection.anki2` while Anki is running — it will SQLITE_BUSY crash Anki.

---

## Implementation: Minimal FastAPI Service

```python
# anki_api.py  — run with: uvicorn anki_api:app --port 9000
import json, urllib.request, base64
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

ANKI = "http://localhost:8765"
app = FastAPI(title="Anki Local API")

def anki(action: str, **params):
    body = json.dumps({"action": action, "version": 6, "params": params}).encode()
    try:
        r = urllib.request.urlopen(urllib.request.Request(ANKI, body), timeout=30)
        res = json.loads(r.read())
    except Exception as e:
        raise HTTPException(502, f"AnkiConnect unreachable: {e}")
    if res.get("error"):
        raise HTTPException(400, res["error"])
    return res["result"]

# ── Rebuild a full deck (generate + import)
@app.post("/deck/rebuild")
def rebuild_deck(deck_name: str):
    import subprocess, sys
    r = subprocess.run([sys.executable, "terminaciones/deploy.py"], capture_output=True, text=True)
    if r.returncode != 0:
        raise HTTPException(500, r.stderr)
    return {"status": "ok", "output": r.stdout}

# ── Update a single note's fields
class FieldUpdate(BaseModel):
    note_id: int
    fields: dict[str, str]

@app.put("/note/fields")
def update_note(body: FieldUpdate):
    anki("updateNoteFields", note={"id": body.note_id, "fields": body.fields})
    return {"updated": body.note_id}

# ── Find notes by query
@app.get("/notes")
def find_notes(q: str):
    ids = anki("findNotes", query=q)
    if not ids:
        return []
    return anki("notesInfo", notes=ids)

# ── Store a media file
class MediaFile(BaseModel):
    filename: str
    data_b64: str  # base64-encoded bytes

@app.post("/media")
def store_media(body: MediaFile):
    anki("storeMediaFile", filename=body.filename, data=body.data_b64)
    return {"stored": body.filename}

# ── Health check (verifies AnkiConnect is up)
@app.get("/health")
def health():
    v = anki("version")
    return {"ankiconnect_version": v, "status": "ok"}
```

Install and run:
```bash
pip install fastapi uvicorn
uvicorn anki_api:app --port 9000 --reload
```

---

## Stable GUID Pattern — Concrete Implementation

Apply this to all deck generators in the project:

```python
# In terminaciones/gen_all_decks.py — replace the Note creation line
# OLD:
deck.add_note(genanki.Note(model=model, fields=[front, back]))

# NEW (in generate_deck function):
identity = f"terminaciones:{deck_id}:{verb_key}:{form_idx_in_tense}"
deck.add_note(StableNote(model=model, fields=[front, back], identity_key=identity))
```

```python
# In compounds/generate_deck.py — replace the Note creation line
# OLD:
note = genanki.Note(model=model, fields=[front, back])

# NEW:
identity = f"compounds:{deck_id}:{lemma}"  # lemma is stable identifier
note = StableNote(model=model, fields=[front, back], identity_key=identity)
```

Place the `StableNote` class in a shared module:
```
koine-anki/
  shared/
    stable_note.py   ← StableNote class + genanki.guid_for wrapper
```

---

## AnkiConnect API Cheat Sheet

All calls: `POST http://localhost:8765` with body `{"action":"...", "version":6, "params":{...}}`

| Action | Params | Returns |
|---|---|---|
| `version` | — | `6` |
| `deckNames` | — | list of deck names |
| `createDeck` | `deck: str` | deck ID |
| `addNote` | `note: {deckName, modelName, fields, tags, options}` | note ID |
| `addNotes` | `notes: [...]` | list of note IDs (null = duplicate) |
| `findNotes` | `query: str` | list of note IDs |
| `notesInfo` | `notes: [id,...]` | list of note objects |
| `updateNoteFields` | `note: {id, fields}` | null |
| `deleteNotes` | `notes: [id,...]` | null |
| `importPackage` | `path: str` (absolute) | null |
| `storeMediaFile` | `filename, data (b64) OR path OR url` | filename |
| `sync` | — | null |
| `multi` | `actions: [...]` | list of results |

**Duplicate guard for addNote**:
```json
"options": {"allowDuplicate": false, "duplicateScope": "deck"}
```

---

## Concurrency Rules for Multi-Agent Writes

1. **Never** write directly to `collection.anki2` while Anki is running.
2. **All writes** must go through AnkiConnect — it serializes via Qt main thread.
3. AnkiConnect processes one request at a time (Python GIL + Qt). No parallel write race
   conditions, but bulk operations are sequential.
4. For batch inserts: use `addNotes` (single request) or `multi` action — NOT N separate
   `addNote` calls.
5. If Anki is **not** running (headless/CI):
   ```python
   from anki.collection import Collection
   col = Collection("/path/to/User 1/collection.anki2")
   # do operations
   col.close()
   ```
   Install with: `pip install anki`

---

## Deck Update Flow (Without Delete Cycle)

```
Current (broken):                     Recommended (fixed):
  generate .apkg                        generate .apkg
  deleteNotes(all in deck)         →    (skip delete)
  importPackage(apkg)                   importPackage(apkg)
                                        # Anki matches by GUID:
                                        #   same GUID + newer = UPDATE (scheduling preserved)
                                        #   new GUID = add new card
```

Anki's `importPackage` compares the `mod` (modification time) stored in the note. genanki sets
`mod` to `int(time.time())` on every build, so every re-import will be seen as "newer" and will
update. **Scheduling history is preserved.**

---

## Media Handling for Audio Cards

```python
# Option A: storeMediaFile with local path (AnkiConnect reads the file itself)
anki("storeMediaFile", filename="my_audio.mp3", path="/abs/path/to/my_audio.mp3")

# Option B: storeMediaFile with base64 (useful for remote/generated audio)
import base64
data = base64.b64encode(Path("my_audio.mp3").read_bytes()).decode()
anki("storeMediaFile", filename="my_audio.mp3", data=data)

# Then in the genanki note field:
fields=["Front text", "Back text [sound:my_audio.mp3]"]
# OR in genanki Package:
pkg = genanki.Package(deck)
pkg.media_files = ["path/to/my_audio.mp3"]  # genanki handles the rename+embed
```

For TTS (current project uses AWS Polly for Spanish, Google TTS for Greek):
- Generate audio → write to temp file → include in `Package.media_files`
- Stable audio filenames: use the same identity key as the GUID (e.g., `audio_terminaciones_deck1_lyow_0.mp3`)

---

## Python Library Comparison

| Library | Use case | Notes |
|---|---|---|
| **genanki** | Generate .apkg from scratch | ✅ Already in use. Override GUID. |
| **AnkiConnect** | CRUD via running Anki | ✅ Already in use. |
| **anki** (official pip) | Headless collection access | Good for CI/batch when Anki closed |
| **ankipandas** | Pandas-based collection analysis | Read-only safe, writes require backup |
| **ankisync2** | .apkg read/edit without genanki | Useful for modifying existing .apkg |
| **apy / apyanki** | CLI wrapper over `anki` pip pkg | For terminal workflows |

---

## Error Handling & Rollback

```python
def safe_import(apkg_path: str) -> bool:
    """Import with pre-flight check and rollback guidance."""
    # 1. Verify AnkiConnect is alive
    try:
        anki("version")
    except Exception:
        print("Anki not running — start Anki first")
        return False

    # 2. Export current deck as backup before overwrite
    # (manual: File → Export → .apkg with scheduling)

    # 3. Import
    anki("importPackage", path=str(Path(apkg_path).resolve()))

    # 4. Verify card count
    count = len(anki("findNotes", query=f"deck:Koiné Griego::Terminaciones"))
    print(f"Cards after import: {count}")
    return True
```

If an import causes problems: File → Import the last known-good `.apkg` backup. Because GUIDs
are stable, this cleanly restores the previous content while preserving any scheduling history
that wasn't overwritten.

---

## Immediate Actions (Prioritized)

### 1. Fix GUIDs (TODAY — 30 min)

Add `stable_note.py` and update all three deck generators. This eliminates duplicates on
re-import immediately.

```bash
# Test: run deploy.py twice. Card count should not grow.
cd /Users/murivirg/work/github/anki/koine-anki/terminaciones
python deploy.py
python deploy.py  # ← should say "updated N notes", not "added N new notes"
```

### 2. Add `/deck/rebuild` endpoint (optional, 1–2 hours)

If you want programmatic triggering (e.g., from another agent or CI):
```bash
pip install fastapi uvicorn
# Add anki_api.py to project root
# curl -X POST http://localhost:9000/deck/rebuild?deck_name=terminaciones
```

### 3. Verify importPackage preserves scheduling

Run once, make one card reviewed (flip it), re-run deploy.py. The reviewed card should still
show as reviewed after the second import. This validates the stable GUID approach is working.

---

## References

- AnkiConnect source (canonical): https://git.sr.ht/~foosoft/anki-connect
- AnkiConnect addon ID: `2055492159`
- genanki GUID docs: https://github.com/kerrickstaley/genanki#note-guids
- AnkiConnect Setup Guide: https://gist.github.com/gwpl/c88c04e7a9c648c49b81a148f07850dd
- Anki import dedup docs: https://docs.ankiweb.net/importing/packaged-decks.html
- Official anki Python pkg: `pip install anki`
