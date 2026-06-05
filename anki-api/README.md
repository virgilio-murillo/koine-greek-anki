# anki-api

Local HTTP API for programmatic Anki deck/card management. Eliminates manual delete→import cycles by using stable GUIDs.

## Requirements

- Anki desktop running with [AnkiConnect](https://ankiweb.net/shared/info/2055492159) addon (port 8765)
- Python 3.11+

## Install & Run

```bash
pip install -e ".[dev]"
uvicorn anki_api.main:app --port 9000 --host 127.0.0.1
```

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Verify AnkiConnect is alive |
| GET | `/decks` | List all decks |
| POST | `/decks` | Create a deck |
| DELETE | `/decks/{name}` | Delete a deck + cards |
| GET | `/notes?q=...` | Find notes by Anki query |
| POST | `/notes` | Add notes (batch) |
| PUT | `/notes/fields` | Update fields on existing note |
| DELETE | `/notes` | Delete notes by IDs |
| POST | `/deck/build-and-import` | Generate .apkg with stable GUIDs + import |
| POST | `/deck/import?path=...` | Import existing .apkg file |
| POST | `/media` | Store media file |
| POST | `/sync` | Trigger Anki sync |

## Key Concept: Stable GUIDs

The `identity_key` parameter ensures re-imports UPDATE existing cards instead of creating duplicates:

```python
# Same identity_key = same card, even if content changes
{"identity_key": "dva:q1", "fields": ["Question?", "Updated answer"]}
```

## Example: Build & Import

```bash
curl -X POST http://localhost:9000/deck/build-and-import \
  -H 'Content-Type: application/json' \
  -d '{
    "deck_name": "My Deck",
    "deck_id": 1234567890,
    "note_model_id": 1234567891,
    "note_model_name": "Basic",
    "note_model_fields": ["Front", "Back"],
    "note_model_templates": [{"name": "Card 1", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr>{{Back}}"}],
    "notes": [
      {"identity_key": "myproject:card1", "fields": ["Q1", "A1"], "tags": ["tag1"]}
    ]
  }'
```

## Tests

```bash
python -m pytest tests/ -v
```
