"""Build .apkg files with stable GUIDs and import via AnkiConnect."""
import tempfile
from pathlib import Path

import genanki

from .stable_note import StableNote


def build_and_import(data: dict, anki_client) -> dict:
    """Generate .apkg with stable GUIDs and import it via AnkiConnect."""
    model = genanki.Model(
        data["note_model_id"],
        data["note_model_name"],
        fields=[{"name": f} for f in data["note_model_fields"]],
        templates=[
            {"name": t.get("name", f"Card {i+1}"), "qfmt": t["qfmt"], "afmt": t["afmt"]}
            for i, t in enumerate(data["note_model_templates"])
        ],
        css=data.get("css", ""),
    )

    deck = genanki.Deck(data["deck_id"], data["deck_name"])

    for note_data in data["notes"]:
        note = StableNote(
            model=model,
            fields=note_data["fields"],
            tags=note_data.get("tags", []),
            identity_key=note_data["identity_key"],
        )
        deck.add_note(note)

    pkg = genanki.Package(deck)
    pkg.media_files = data.get("media_files", [])

    with tempfile.NamedTemporaryFile(suffix=".apkg", delete=False) as f:
        pkg.write_to_file(f.name)
        apkg_path = f.name

    anki_client.call("importPackage", path=str(Path(apkg_path).resolve()))
    Path(apkg_path).unlink()

    return {"imported": len(data["notes"]), "deck": data["deck_name"]}
