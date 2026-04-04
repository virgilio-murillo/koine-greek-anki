# Koine Greek Compound Words — Anki Deck Project

## What This Is
Anki decks that teach Koine Greek compound words by decomposing them into their parts (prefix + root + suffix) with full etymological context, Strong's references, and mnemonics in Spanish.

## Current Status
- ✅ **Matthew**: 290 compound words → `decks/matthew_compounds.apkg`
- ⬜ Mark through Revelation: ready to generate (pipeline exists)
- ⬜ Septuagint (LXX): data source identified, not yet processed

## User Profile
- Native Spanish speaker, also speaks English
- Learning Koine Greek as a beginner
- Card explanations in **Spanish**
- Does NOT know formal grammar terminology — explain simply
- Wants cards to be **100% self-contained** — no need to look anything up elsewhere

## Quick Start: Generate a New Book
```bash
source venv/bin/activate
# 1. Extract compounds from a book (1=Matthew, 2=Mark, ..., 27=Revelation)
python src/extract_compounds.py --book 2 --output data/mark/compounds_raw.json

# 2. [MANUAL STEP] Decompose compounds — requires LLM analysis
#    See notes/compounds-pipeline.md for the full process

# 3. Enrich with Strong's + suffixes
python src/enrich_compounds.py

# 4. Generate deck
python src/generate_deck.py
```

## Folder Structure
```
├── src/                    # Pipeline scripts (reproducible)
│   ├── extract_compounds.py    # Extract compound candidates from MorphGNT
│   ├── enrich_compounds.py     # Add suffix explanations + root-change notes
│   ├── fetch_strongs.py        # Fetch Strong's etymology for words + components
│   ├── improve_mnemonics.py    # Improve short/unhelpful mnemonics
│   └── generate_deck.py        # Generate .apkg with genanki
├── data/
│   ├── strongs_greek.xml       # Strong's Greek dictionary (5516 entries)
│   ├── compounds_registry.json # Anti-duplicate registry (tracks processed words)
│   ├── morphology_reference.md # Greek suffix/prefix/ablaut reference
│   ├── morphology_context.md   # Detailed morphology analysis
│   └── matthew/                # Per-book data
│       ├── compounds_raw.json      # Raw candidates from extraction
│       └── compounds_enriched.json # Final enriched data (290 entries)
├── decks/                  # Output .apkg files
├── notes/                  # Guidelines, pipeline docs, lessons learned
├── old/                    # Previous projects (pronouns deck, etc.)
└── venv/                   # Python 3.12 venv (genanki, py-sblgnt)
```

## Data Sources
| Source | URL | What |
|--------|-----|------|
| MorphGNT/SBLGNT | `pip install py-sblgnt` | NT text with lemmas, morphology, verse refs |
| Strong's Greek Dictionary | `morphgnt/strongs-dictionary-xml` on GitHub | Etymology + definitions for 5516 NT words |
| LXX Lemmas | `openscriptures/GreekResources/LxxLemmas/` on GitHub | 60 books of Septuagint, lemmatized JSON |

## Dependencies
```
pip install genanki py-sblgnt
```
