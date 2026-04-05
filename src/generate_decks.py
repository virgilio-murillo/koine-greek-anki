"""Generate Anki decks — 4 cards per lesson, 10 lessons per deck, under parent deck."""
import genanki, random, html, os, sys
sys.path.insert(0, ".")
from src.data import ALL_LESSONS

random.seed(42)

MODEL = genanki.Model(
    1646410900000,
    "Koiné Pimsleur",
    fields=[{"name": "Greek"}, {"name": "Spanish"}, {"name": "Lesson"}, {"name": "Type"}],
    templates=[{
        "name": "Recognition",
        "qfmt": '<div class="greek">{{Greek}}</div><div class="meta">Lección {{Lesson}} · {{Type}}</div>',
        "afmt": '{{FrontSide}}<hr id="answer"><div class="spanish">{{Spanish}}</div>',
    }, {
        "name": "Production",
        "qfmt": '<div class="spanish">{{Spanish}}</div><div class="meta">Lección {{Lesson}} · {{Type}}</div>',
        "afmt": '{{FrontSide}}<hr id="answer"><div class="greek">{{Greek}}</div>',
    }],
    css=""".card{font-family:Georgia,serif;font-size:20px;text-align:center;background:#fafaf5;padding:20px}
.greek{font-size:36px;color:#1a3a5c;margin:15px 0}
.spanish{font-size:28px;color:#2d6a2e;margin:15px 0}
.meta{font-size:13px;color:#999;font-style:italic}"""
)

PARENT = "Koiné Griego"
DECK_CONFIGS = [
    (1, 10, "L01-10 Saludos y Bases"),
    (11, 20, "L11-20 Vida Cotidiana y Fe"),
    (21, 30, "L21-30 Cultura y Oración"),
]

os.makedirs("decks/anki", exist_ok=True)
h = html.escape

for lo, hi, name in DECK_CONFIGS:
    deck_name = f"{PARENT}::{name}"
    deck_id = 1646410900000 + lo
    deck = genanki.Deck(deck_id, deck_name)

    for L in ALL_LESSONS[lo-1:hi]:
        n = L["num"]
        vocab = L["vocab"]
        phrases = L["phrases"]
        # Pick 4: first 2 vocab + first phrase + verse
        cards = []
        for v in vocab[:2]:
            cards.append((v["gr"], v["es"], "vocabulario"))
        if phrases:
            cards.append((phrases[0]["gr"], phrases[0]["es"], "frase"))
        verse = L.get("verse", {})
        if verse and len(cards) < 4:
            cards.append((verse["gr"], verse.get("explain_es", "")[:80], "versículo"))
        # Fill to 4 if needed
        for v in vocab[2:]:
            if len(cards) >= 4: break
            cards.append((v["gr"], v["es"], "vocabulario"))

        for gr_text, es_text, typ in cards[:4]:
            note = genanki.Note(model=MODEL, fields=[h(gr_text), h(es_text), str(n), typ])
            deck.add_note(note)

    out = f"decks/anki/{name.replace(' ', '_').lower()}.apkg"
    genanki.Package(deck).write_to_file(out)
    count = hi - lo + 1
    print(f"✓ {out} — {count * 4} cards ({count} lessons × 4)")
