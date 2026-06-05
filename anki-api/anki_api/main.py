"""Anki Local API — FastAPI service wrapping AnkiConnect."""
from pathlib import Path

from fastapi import FastAPI, HTTPException, Query

from .anki_client import AnkiClient, AnkiConnectError
from .deck_builder import build_and_import
from .models import (
    DeckBuildImport,
    DeckCreate,
    FieldsUpdate,
    MediaStore,
    NoteCreate,
    NotesBatchCreate,
    NotesDelete,
)

app = FastAPI(title="Anki Local API", version="0.1.0")
client = AnkiClient()


def _handle(action: str, **params):
    try:
        return client.call(action, **params)
    except AnkiConnectError as e:
        raise HTTPException(502, str(e))


# ── Health ──
@app.get("/health")
def health():
    v = _handle("version")
    return {"status": "ok", "ankiconnect_version": v}


# ── Decks ──
@app.get("/decks")
def list_decks():
    return _handle("deckNames")


@app.post("/decks", status_code=201)
def create_deck(body: DeckCreate):
    deck_id = _handle("createDeck", deck=body.name)
    return {"deck_id": deck_id, "name": body.name}


@app.delete("/decks/{name}")
def delete_deck(name: str):
    _handle("deleteDecks", decks=[name], cardsToo=True)
    return {"deleted": name}


# ── Notes ──
@app.get("/notes")
def find_notes(q: str = Query(..., description="Anki search query")):
    ids = _handle("findNotes", query=q)
    if not ids:
        return []
    return _handle("notesInfo", notes=ids)


@app.post("/notes", status_code=201)
def add_notes(body: NotesBatchCreate):
    notes = []
    for n in body.notes:
        notes.append({
            "deckName": n.deck_name,
            "modelName": n.model_name,
            "fields": n.fields,
            "tags": n.tags,
            "options": {"allowDuplicate": False, "duplicateScope": "deck"},
        })
    results = _handle("addNotes", notes=notes)
    return {"note_ids": results}


@app.put("/notes/fields")
def update_fields(body: FieldsUpdate):
    _handle("updateNoteFields", note={"id": body.note_id, "fields": body.fields})
    return {"updated": body.note_id}


@app.delete("/notes")
def delete_notes(body: NotesDelete):
    _handle("deleteNotes", notes=body.note_ids)
    return {"deleted": len(body.note_ids)}


# ── Build & Import ──
@app.post("/deck/build-and-import")
def deck_build_and_import(body: DeckBuildImport):
    try:
        result = build_and_import(body.model_dump(), client)
    except AnkiConnectError as e:
        raise HTTPException(502, str(e))
    return result


@app.post("/deck/import")
def deck_import(path: str = Query(..., description="Absolute path to .apkg file")):
    p = Path(path).resolve()
    if not p.exists():
        raise HTTPException(404, f"File not found: {p}")
    _handle("importPackage", path=str(p))
    return {"imported": str(p)}


# ── Media ──
@app.post("/media", status_code=201)
def store_media(body: MediaStore):
    params = {"filename": body.filename}
    if body.data_b64:
        params["data"] = body.data_b64
    elif body.path:
        params["path"] = body.path
    else:
        raise HTTPException(400, "Provide either data_b64 or path")
    _handle("storeMediaFile", **params)
    return {"stored": body.filename}


# ── Sync ──
@app.post("/sync")
def sync():
    _handle("sync")
    return {"status": "synced"}
