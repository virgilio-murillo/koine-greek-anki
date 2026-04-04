# Koine Greek — Anki Decks + Pimsleur Audio Course

Two complementary tools for learning Koine Greek (the language of the New Testament):

1. **Anki Deck**: 290 compound word flashcards with etymological decomposition, Strong's references, and mnemonics in Spanish
2. **Pimsleur Audio Course**: 90 lessons (16.7 hours) teaching ~600 words covering ~90% of the NT text

## Anki Deck — Compound Words

Flashcards that teach Greek compound words by breaking them into parts:
- Front: the compound word (e.g., ἀποκαλύπτω)
- Back: components (ἀπό "away" + καλύπτω "cover" = "uncover, reveal"), Strong's etymology, suffix explanation, mnemonic in Spanish

```bash
# Generate the deck
source venv/bin/activate
python src/generate_deck.py
```

## Pimsleur Audio Course — 90 Lessons

Audio lessons using the Pimsleur method (anticipation, graduated interval recall) set in 1st century Palestine with biblical scenarios.

See [audio/README.md](audio/README.md) for full structure and lesson details.

| Level | Lessons | Hours | Words | NT Coverage |
|---|---|---|---|---|
| 1 — Ὁ Ξένος | 1-30 | ~5.5 | ~200 | ~75% |
| 2 — Ὁ Μαθητής | 31-60 | ~5.5 | ~400 | ~85% |
| 3 — Ὁ Κήρυξ | 61-90 | ~5.7 | ~600 | ~90% |

## Data Sources

| Source | What | License |
|---|---|---|
| MorphGNT/SBLGNT | NT text with lemmas + morphology | MIT |
| Strong's Greek Dictionary | Etymology for 5516 NT words | Public domain |
| openscriptures/LxxLemmas | Septuagint lemmatized (60 books) | Open |

## Tech Stack

- **Spanish narration**: Amazon Polly (Mia, es-MX, neural)
- **Greek speech**: Google Cloud TTS (Chirp3-HD + Wavenet-B fallback)
- **Audio assembly**: Python (pydub + ffmpeg)
- **Anki generation**: genanki
- **NT corpus**: py-sblgnt

## Project Structure

```
├── audio/                  90 lesson MP3s organized by level
├── src/                    Pipeline scripts
│   ├── pimsleur_engine.py      Audio generation engine
│   ├── lesson_data_*.py        Lesson content (90 lessons)
│   ├── extract_compounds.py    Anki: extract compounds from NT
│   ├── enrich_compounds.py     Anki: add Strong's + suffixes
│   └── generate_deck.py        Anki: generate .apkg
├── data/                   NT text, Strong's dictionary, frequency lists
├── notes/                  Curriculum, guidelines, lessons learned
└── decks/                  Generated .apkg files
```

## Quick Start

```bash
python3 -m venv venv && source venv/bin/activate
pip install genanki py-sblgnt google-cloud-texttospeech boto3 pydub
brew install ffmpeg
```
