# Anki Integration

This project (FROZEN — no edits to existing code) can use `anki-api` to manage its decks.

## Prerequisites

- Anki desktop running with [AnkiConnect](https://ankiweb.net/shared/info/2055492159) addon
- `anki-api` CLI installed (`pip install -e ~/work/github/anki/anki-api`)

## Usage

### Import existing .apkg files

```bash
anki-api deck import DVA-C02_Questions.txt    # if converted to .apkg
anki-api deck import SAW/SAW_Topics4-9.apkg
```

### Query existing cards

```bash
anki-api notes find "deck:DVA-C02"
anki-api notes find "deck:SAW"
```

### Sync to AnkiWeb

```bash
anki-api sync
```

## Note

This repo is FROZEN. For new Anki card work, use `koine-anki/` or create JSON specs in the appropriate course project and use `anki-api deck sync --file spec.json`.
