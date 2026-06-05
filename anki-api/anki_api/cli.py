"""CLI for anki-api. Talks directly to AnkiConnect."""
import argparse
import json
import sys
import tempfile
from pathlib import Path

from .anki_client import AnkiClient, AnkiConnectError
from .deck_builder import build_and_import


client = AnkiClient()


def _out(data):
    json.dump(data, sys.stdout, ensure_ascii=False, indent=2)
    print()


def _err(msg):
    json.dump({"error": str(msg)}, sys.stderr, ensure_ascii=False)
    print(file=sys.stderr)
    sys.exit(1)


def cmd_health(_args):
    v = client.call("version")
    _out({"status": "ok", "ankiconnect_version": v})


def cmd_decks_list(_args):
    _out(client.call("deckNames"))


def cmd_decks_create(args):
    deck_id = client.call("createDeck", deck=args.name)
    _out({"deck_id": deck_id, "name": args.name})


def cmd_decks_delete(args):
    client.call("deleteDecks", decks=[args.name], cardsToo=True)
    _out({"deleted": args.name})


def cmd_notes_find(args):
    ids = client.call("findNotes", query=args.query)
    if not ids:
        _out([])
        return
    _out(client.call("notesInfo", notes=ids))


def cmd_notes_add(args):
    fields = json.loads(args.fields)
    notes = [{
        "deckName": args.deck,
        "modelName": args.model,
        "fields": fields,
        "tags": args.tags.split(",") if args.tags else [],
        "options": {"allowDuplicate": False, "duplicateScope": "deck"},
    }]
    result = client.call("addNotes", notes=notes)
    _out({"note_ids": result})


def cmd_notes_update(args):
    fields = json.loads(args.fields)
    client.call("updateNoteFields", note={"id": args.id, "fields": fields})
    _out({"updated": args.id})


def cmd_notes_delete(args):
    ids = [int(x) for x in args.ids.split(",")]
    client.call("deleteNotes", notes=ids)
    _out({"deleted": len(ids)})


def cmd_deck_build_and_import(args):
    spec = json.loads(Path(args.file).read_text())
    result = build_and_import(spec, client)
    _out(result)


def cmd_deck_sync(args):
    """Smart sync: import new cards via .apkg, update existing via updateNoteFields."""
    from .deck_builder import build_and_import
    spec = json.loads(Path(args.file).read_text())

    # First import to create any new cards
    build_and_import(spec, client)

    # Then update all existing cards' fields via AnkiConnect
    deck_name = spec["deck_name"]
    existing_ids = client.call("findNotes", query=f"deck:{deck_name}")
    existing_notes = client.call("notesInfo", notes=existing_ids) if existing_ids else []

    # Build a map of first-field-value → note_id for matching
    existing_map = {}
    for n in existing_notes:
        fields = n["fields"]
        first_field = list(fields.values())[0]["value"]
        existing_map[first_field] = n["noteId"]

    updated = 0
    field_names = spec["note_model_fields"]
    for note_data in spec["notes"]:
        field_values = note_data["fields"]
        first_val = field_values[0]
        if first_val in existing_map:
            note_id = existing_map[first_val]
            fields_dict = {field_names[i]: field_values[i] for i in range(len(field_values))}
            client.call("updateNoteFields", note={"id": note_id, "fields": fields_dict})
            updated += 1

    _out({"deck": deck_name, "total": len(spec["notes"]), "updated": updated})


def cmd_deck_import(args):
    p = Path(args.path).resolve()
    if not p.exists():
        _err(f"File not found: {p}")
    client.call("importPackage", path=str(p))
    _out({"imported": str(p)})


def cmd_media_store(args):
    params = {"filename": args.filename}
    if args.path:
        params["path"] = str(Path(args.path).resolve())
    elif args.data_b64:
        params["data"] = args.data_b64
    else:
        _err("Provide --path or --data-b64")
    client.call("storeMediaFile", **params)
    _out({"stored": args.filename})


def cmd_sync(_args):
    client.call("sync")
    _out({"status": "synced"})


def main():
    p = argparse.ArgumentParser(prog="anki-api", description="Anki management CLI")
    sub = p.add_subparsers(dest="command", required=True)

    # health
    sub.add_parser("health")

    # decks
    decks = sub.add_parser("decks")
    decks_sub = decks.add_subparsers(dest="subcommand", required=True)
    decks_sub.add_parser("list")
    dc = decks_sub.add_parser("create")
    dc.add_argument("name")
    dd = decks_sub.add_parser("delete")
    dd.add_argument("name")

    # notes
    notes = sub.add_parser("notes")
    notes_sub = notes.add_subparsers(dest="subcommand", required=True)
    nf = notes_sub.add_parser("find")
    nf.add_argument("query")
    na = notes_sub.add_parser("add")
    na.add_argument("--deck", required=True)
    na.add_argument("--model", required=True)
    na.add_argument("--fields", required=True, help="JSON object")
    na.add_argument("--tags", default="")
    na.add_argument("--key", dest="identity_key", default="")
    nu = notes_sub.add_parser("update")
    nu.add_argument("--id", type=int, required=True)
    nu.add_argument("--fields", required=True, help="JSON object")
    nd = notes_sub.add_parser("delete")
    nd.add_argument("--ids", required=True, help="Comma-separated note IDs")

    # deck
    deck = sub.add_parser("deck")
    deck_sub = deck.add_subparsers(dest="subcommand", required=True)
    dbi = deck_sub.add_parser("build-and-import")
    dbi.add_argument("--file", required=True, help="Path to JSON spec file")
    ds = deck_sub.add_parser("sync")
    ds.add_argument("--file", required=True, help="Path to JSON spec file")
    di = deck_sub.add_parser("import")
    di.add_argument("path")

    # media
    media = sub.add_parser("media")
    media_sub = media.add_subparsers(dest="subcommand", required=True)
    ms = media_sub.add_parser("store")
    ms.add_argument("--filename", required=True)
    ms.add_argument("--path", default=None)
    ms.add_argument("--data-b64", default=None)

    # sync
    sub.add_parser("sync")

    args = p.parse_args()

    try:
        dispatch = {
            "health": cmd_health,
            "decks": lambda a: {"list": cmd_decks_list, "create": cmd_decks_create, "delete": cmd_decks_delete}[a.subcommand](a),
            "notes": lambda a: {"find": cmd_notes_find, "add": cmd_notes_add, "update": cmd_notes_update, "delete": cmd_notes_delete}[a.subcommand](a),
            "deck": lambda a: {"build-and-import": cmd_deck_build_and_import, "sync": cmd_deck_sync, "import": cmd_deck_import}[a.subcommand](a),
            "media": lambda a: {"store": cmd_media_store}[a.subcommand](a),
            "sync": cmd_sync,
        }
        dispatch[args.command](args)
    except AnkiConnectError as e:
        _err(e)


if __name__ == "__main__":
    main()
