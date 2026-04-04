"""Generate Anki deck from enriched compound words data."""
import json, genanki, random, html

random.seed(42)
MODEL_ID = 1646410861300
DECK_ID = 1646410861301

with open("data/matthew/compounds_enriched.json") as f:
    cards = json.load(f)

# Model with Front/Back fields
model = genanki.Model(
    MODEL_ID,
    "Greek Compounds",
    fields=[
        {"name": "Front"},
        {"name": "Back"},
    ],
    templates=[{
        "name": "Card 1",
        "qfmt": "{{Front}}",
        "afmt": '{{FrontSide}}<hr id="answer">{{Back}}',
    }],
    css="""
.card { font-family: 'Georgia', 'Times New Roman', serif; font-size: 18px; text-align: left; color: #333; background: #fafaf5; padding: 20px; line-height: 1.6; }
.word { font-size: 36px; color: #1a3a5c; text-align: center; margin: 10px 0; }
.meaning { font-size: 22px; color: #2d6a2e; text-align: center; margin: 5px 0 15px 0; }
.ref { font-size: 13px; color: #999; text-align: center; font-style: italic; }
.strongs { font-size: 13px; color: #888; text-align: center; margin-bottom: 15px; }
.section { margin: 12px 0; padding: 10px 12px; background: #f0efe8; border-left: 3px solid #c0b890; border-radius: 4px; }
.section-title { font-weight: bold; color: #5a4e3a; font-size: 14px; margin-bottom: 6px; }
.comp-box { margin: 6px 0; padding: 8px 10px; background: #fff; border: 1px solid #ddd; border-radius: 4px; }
.comp-greek { font-size: 20px; color: #1a3a5c; }
.comp-meaning { color: #2d6a2e; font-weight: bold; }
.comp-detail { font-size: 13px; color: #666; margin-top: 3px; }
.suffix-box { margin: 8px 0; padding: 8px 10px; background: #f5f0ff; border-left: 3px solid #9b8ec4; border-radius: 4px; }
.root-box { margin: 8px 0; padding: 8px 10px; background: #fff8f0; border-left: 3px solid #d4a054; border-radius: 4px; }
.mnemonic { margin: 12px 0; padding: 12px; background: #f0f7f0; border-left: 3px solid #6aaa6a; border-radius: 4px; font-size: 16px; }
.etymology { font-size: 13px; color: #555; font-style: italic; margin-top: 4px; }
"""
)

deck = genanki.Deck(DECK_ID, "Koiné Griego – Palabras Compuestas (Mateo)")

def h(text):
    return html.escape(text) if text else ""

def build_back(c):
    parts = []

    # Word + meaning + ref
    parts.append(f'<div class="word">{h(c["lemma"])}</div>')
    parts.append(f'<div class="meaning">{h(c["meaning_es"])}</div>')
    ref = c.get("first_ref", "")
    snum = c.get("strongs_number", "")
    parts.append(f'<div class="ref">{h(ref)}{" · " + h(snum) if snum else ""}</div>')

    # Strong's derivation
    sd = c.get("strongs_derivation", "")
    sdef = c.get("strongs_definition", "")
    if sd or sdef:
        combined = f"{sd} — {sdef}" if sd and sdef else sd or sdef
        combined = " ".join(combined.split())
        parts.append(f'<div class="strongs">Strong\'s: {h(combined)}</div>')

    # Components
    parts.append('<div class="section"><div class="section-title">📦 Componentes</div>')
    for comp in c["components"]:
        g = comp["greek"]
        m = comp["meaning_es"]
        parts.append(f'<div class="comp-box">')
        parts.append(f'<span class="comp-greek">{h(g)}</span> — <span class="comp-meaning">{h(m)}</span>')
        csnum = comp.get("strongs_number", "")
        if csnum:
            parts.append(f' <span style="color:#aaa;font-size:12px">({h(csnum)})</span>')
        cdef = comp.get("strongs_definition", "")
        if cdef:
            cdef_clean = " ".join(cdef.split())[:200]
            parts.append(f'<div class="comp-detail">{h(cdef_clean)}</div>')
        parts.append('</div>')
    parts.append('</div>')

    # Suffix explanation
    if "suffix" in c:
        parts.append(f'<div class="suffix-box">')
        parts.append(f'<div class="section-title">🔤 Sufijo: {h(c["suffix"])} ({h(c["suffix_type_es"])})</div>')
        parts.append(f'{h(c["suffix_explanation_es"])}')
        parts.append('</div>')

    # Root change note
    if "root_note_es" in c:
        parts.append(f'<div class="root-box">')
        parts.append(f'<div class="section-title">🔀 Cambio de raíz</div>')
        parts.append(f'{h(c["root_note_es"])}')
        parts.append('</div>')

    # Mnemonic
    parts.append(f'<div class="mnemonic">')
    parts.append(f'<div class="section-title">💡 Mnemotecnia</div>')
    parts.append(f'{h(c["mnemonic_es"])}')
    parts.append('</div>')

    return "\n".join(parts)

for c in cards:
    front = f'<div class="word">{h(c["lemma"])}</div><div class="ref" style="margin-top:8px">¿De qué se compone esta palabra?</div>'
    back = build_back(c)
    note = genanki.Note(model=model, fields=[front, back])
    deck.add_note(note)

output = "decks/matthew_compounds.apkg"
genanki.Package(deck).write_to_file(output)
print(f"Generated {len(cards)} cards → {output}")
