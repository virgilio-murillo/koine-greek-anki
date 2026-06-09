# Investigation Findings: Enhance anki-agent

## 1. What's in Each Subdirectory

### `anki-main/` — Original Monorepo (now superseded)
The original combined workspace. Contains:
- `languages/` — the full project before it was split into koine-anki + koine-pimsleur
- `SAW/` — unrelated Anki decks (Solutions Architect Workshop)
- `DVA-C02_Questions.txt` — AWS cert prep (unrelated)
- Has its own `venv/`, `src/`, `data/`, `decks/`, `notes/`, `audio/`
- **Status**: Appears to be the "origin" repo; koine-anki and koine-pimsleur were extracted from it

### `koine-anki/` — Flashcard Deck Generation (Active)
Focused on Anki flashcard creation for Koine Greek:
- **`compounds/`** — Pipeline for compound word cards (290 cards from Matthew, 4233 in full NT+LXX)
  - `extract_compounds.py` → `fetch_strongs.py` → `enrich_compounds.py` → `enrich_cognates.py` → `enrich_verses.py` → `add_rvr60.py` → `improve_mnemonics.py` → `generate_deck.py`
  - `audit_cognates.py` — quality check on cognate data
- **`terminaciones/`** — Grammar endings flashcards (verb conjugations, infinitives, participles)
  - `cards_cat1.py` through `cards_cat7.py` — Vol 2 (text export)
  - `cards_vol3_cat1.py` through `cards_vol3_cat7.py` — Vol 3 (.apkg)
  - `gen_deck.py` (TSV output), `gen_deck_vol3.py` (genanki .apkg output)
- **`data/`** — NT corpus and linguistic reference data (shared with koine-pimsleur)
  - `nt-morphgnt/` — 27 NT books morphologically tagged (MorphGNT/SBLGNT, MIT license)
  - `strongs_greek.xml` — Strong's Greek Dictionary (public domain)
  - `nt_vocabulary_frequency.json` — Word frequencies (506KB)
  - `nt_top600.json` — Top 600 NT words with rank/lemma/count/pos
  - `nt_compounds_full.json` — 4,233 compound words (full NT+LXX)
  - `compounds_registry.json` — Deduplication registry (lemma → source_book)
  - `matthew/compounds_enriched.json` — 290 enriched cards for Matthew
  - `es_rvr.json` — Full Spanish Bible (RVR60, 66 books, 4MB)
  - `morphology_reference.md` — Comprehensive suffix/prefix reference
  - `morphology_context.md` — Additional grammar context
  - `pronunciation.csv` — Pronunciation data
  - `nt_grammar_stats.json` — Grammar statistics
- **`notes/`** — Guidelines and documentation
  - `koine-greek-anki-guidelines.md` — Card design principles, user profile, grammar reference
  - `compounds-pipeline.md` — Full reproduction guide for the pipeline
  - `card-quality-standards.md` — Non-negotiable rules for card quality
- **`decks/`** — Generated .apkg output files
- **`kiro-test/`** — Test/scratch area (gitignored)

### `koine-pimsleur/` — Audio Course Generation (Active)
90-lesson Pimsleur-style audio course for Koine Greek:
- **`src/`** — Generation pipeline
  - `engine.py` — Audio generation engine (Pimsleur method: GIR cycles, phrase building)
  - `tts.py` — TTS module (Amazon Polly for Spanish, Google Cloud TTS for Greek)
  - `generate.py` — Lesson generator CLI
  - `render.py` — MP3 renderer
  - `script_builder.py` — Script generator
  - `enrich.py` — LLM enrichment using koine-anki data (Amazon Bedrock/Claude)
  - `generate_decks.py` — Anki deck generator from lesson vocab
  - `data/` — 90 lessons in Python dicts (lesson_data_01_05.py through lesson_data_86_90.py)
- **`audio/`** — 90 lesson MP3s organized by level (3 levels × 30 lessons)
- **`decks/`** — Generated outputs (.apkg, .mp3)
- **`notes/`** — Curriculum docs, lessons learned
- **`serve_audio.py`** — HTTPS server for phone playback

## 2. Deck Generation Tools

| Tool | Location | Input | Output | Library |
|------|----------|-------|--------|---------|
| `generate_deck.py` | koine-anki/compounds/ | `data/matthew/compounds_enriched.json` | `.apkg` (290 cards) | genanki |
| `gen_deck.py` | koine-anki/terminaciones/ | `cards_cat1-7.py` modules | TSV text file | none (raw write) |
| `gen_deck_vol3.py` | koine-anki/terminaciones/ | `cards_vol3_cat1-7.py` modules | `.apkg` | genanki |
| `generate_decks.py` | koine-pimsleur/src/ | `src/data/ALL_LESSONS` | `.apkg` (4 cards/lesson) | genanki |

### Compounds Pipeline (most complex):
```
extract_compounds.py (py-sblgnt → raw candidates)
    → fetch_strongs.py (add Strong's etymology)
    → enrich_compounds.py (add suffix/root explanations)
    → enrich_cognates.py (add Spanish/English/French cognates)
    → enrich_verses.py (add Greek NT verses from MorphGNT)
    → add_rvr60.py (add Spanish Bible translation to verses)
    → improve_mnemonics.py (LLM-improve short mnemonics)
    → generate_deck.py (create .apkg)
```

### Pimsleur Audio Pipeline:
```
lesson_data_*.py (structured content)
    → engine.py (auto-generates GIR cycles, phrase building, reconstruction)
    → tts.py (Polly for Spanish, Google TTS for Greek)
    → pydub assembly → MP3
```

## 3. Relationship to bible-tools / koine-anki/data/

`koine-pimsleur` **depends on** `koine-anki/data/` for:
- `matthew/compounds_enriched.json` — compound word data for enriching lesson scripts
- `morphology_reference.md` — grammar reference for LLM enrichment context
- Connection via `KOINE_ANKI_PATH` env var or sibling directory detection

The `data/` directory serves as a **shared linguistic database**:
- **MorphGNT** (MIT) — morphologically tagged NT text (lemma, POS, morphology code per word)
- **Strong's Greek Dictionary** (public domain) — etymology for 5,516 NT words
- **LXX Lemmas** (open) — Septuagint lemmatized (referenced for future expansion)
- **RVR60** — Full Spanish Bible for verse translations
- **Frequency lists** — Data-driven vocabulary selection

The `nt_compounds_full.json` (4,233 entries) represents the full NT+LXX compound word database, while `matthew/compounds_enriched.json` (290 entries) is the fully enriched subset with verses, cognates, and mnemonics.

## 4. Formats Used

### Data Formats
| Format | File | Structure |
|--------|------|-----------|
| MorphGNT | `*.txt` | Space-separated: `BBCCVV POS morph-code text normalized lemma` |
| Compounds enriched | `.json` | Array of `{lemma, components[], meaning_es, mnemonic_es, strongs_*, suffix*, root_note_es, cognates_by_part{}, greek_verses[]}` |
| Compounds full | `.json` | Array of `{lemma, components[], meaning_es, root_note_es}` |
| Frequency list | `.json` | Array of `{rank, lemma, count, pos}` |
| Registry | `.json` | Map of `lemma → {source_book, deck, date_added}` |
| Spanish Bible | `.json` | Array of `{abbrev, name, chapters[][]}` (66 books) |
| Lesson data | `.py` | Python dicts with `{num, intro_es, dialogue, vocab[], phrases[], recon[], verse, closing_es}` |
| Terminaciones cards | `.py` | Python lists of `(front_html, back_html)` tuples |
| Strong's | `.xml` | XML dictionary (2.3MB) |
| Pronunciation | `.csv` | CSV format |

### Output Formats
- `.apkg` — Anki package (zip containing SQLite + media)
- `.txt` (TSV) — Tab-separated front/back for Anki text import
- `.mp3` — Audio lessons
- `.json` — Enriched lesson scripts

## 5. What the Enhanced Prompt Should Contain

Based on the project structure, existing guidelines, and shared learnings, the enhanced agent prompt should include:

### Critical Rules (highest ROI per shared learnings)
1. **Greek text MUST use NFC normalization** — polytonic Greek has multiple Unicode representations
2. **Verify all Greek against MorphGNT/LXX corpus** — no Modern Greek contamination
3. **All explanations in Spanish** — user is native Spanish speaker
4. **Cards must be 100% self-contained** — never require external lookup
5. **Every morpheme must be explained** — prefix, root, AND suffix
6. **Mnemonics must tell a story** — not just translate components
7. **Use simplified terminology** — avoid formal grammar jargon (see terminology table in guidelines)

### Project Context
- **Three subdirectories**: koine-anki (flashcards), koine-pimsleur (audio course), anki-main (legacy)
- **koine-pimsleur depends on koine-anki/data/** via `KOINE_ANKI_PATH` env var
- **Python 3.12** with genanki, py-sblgnt, google-cloud-texttospeech, boto3, pydub
- **TTS**: Amazon Polly (Mia, es-MX) for Spanish, Google Cloud TTS (Chirp3-HD + Wavenet-B fallback) for Greek
- **LLM**: Amazon Bedrock (Claude) for enrichment

### Key Data Paths
- NT corpus: `koine-anki/data/nt-morphgnt/`
- Strong's: `koine-anki/data/strongs_greek.xml`
- Frequency: `koine-anki/data/nt_vocabulary_frequency.json`
- Top 600: `koine-anki/data/nt_top600.json`
- Compounds (full): `koine-anki/data/nt_compounds_full.json` (4,233 entries)
- Compounds (enriched): `koine-anki/data/matthew/compounds_enriched.json` (290 entries)
- Spanish Bible: `koine-anki/data/es_rvr.json`
- Registry: `koine-anki/data/compounds_registry.json`
- Lessons: `koine-pimsleur/src/data/lesson_data_*.py` (90 lessons)

### Pipeline Commands
```bash
# Compounds deck
cd koine-anki && python compounds/generate_deck.py

# Terminaciones (text)
cd koine-anki && python terminaciones/gen_deck.py

# Terminaciones Vol.3 (.apkg)
cd koine-anki && python terminaciones/gen_deck_vol3.py

# Pimsleur lesson generation
cd koine-pimsleur && python -m src.generate --lesson 5

# Pimsleur Anki decks
cd koine-pimsleur && python src/generate_decks.py

# Enrich lesson with LLM
cd koine-pimsleur && python src/enrich.py kiro-test/lesson_01_script.json
```

### Card Design Standards (from notes/card-quality-standards.md)
- Front: Greek word (36px, dark blue) + question prompt
- Back sections: Word+meaning → 📦 Componentes → 🔤 Sufijo → 🔀 Cambio de raíz → 💡 Mnemotecnia → 🌍 Cognados → 📖 Versículos
- Include Strong's data for compound AND each component
- When etymology is opaque, explain the semantic chain step by step
- Include Spanish/English/French cognates when available

### Koine vs Modern Greek Contamination Rules
- **Vocabulary blacklist**: νερό→ὕδωρ, σπίτι→οἶκος, ψωμί→ἄρτος, πόρτα→θύρα
- **False friends**: παρακαλέω="beseech" not "please", δουλεύω="be a slave" not "work"
- **Grammar Koine has that Modern lost**: dative case, infinitive, synthetic future, genitive absolute, declined participles
- **Verification**: Check all Greek words against MorphGNT + LXX lemma lists

### TTS Technical Notes
- `to_mono()` strips polytonic → monotonic before TTS
- Chirp3-HD fails on short words (1-2 syllables) → fallback to Wavenet-B if audio < 400ms
- All TTS cached by content hash in /tmp/tts_cache/

### Anti-Duplication System
- `compounds_registry.json` tracks processed lemmas by source book
- When processing new books, filter out lemmas already in registry
- 4,233 compounds available in `nt_compounds_full.json` for future deck generation

### Pimsleur Method Structure (per lesson)
1. Opening dialogue (2 min) — student listens
2. Review previous lessons (3 min) — GIR from earlier
3. New vocabulary (7 min) — 5-8 words, back-chaining
4. Phrase building + GIR cycle 1 (6 min)
5. GIR cycle 2 — all vocab shuffled (4 min)
6. Dialogue reconstruction (5 min)
7. Rapid fire GIR cycle 3 (2 min)
8. Biblical verse + closing (1 min)

---

## Sources
- `koine-anki/README.md` — project overview
- `koine-pimsleur/README.md` — audio course overview
- `koine-anki/notes/koine-greek-anki-guidelines.md` — card design principles
- `koine-anki/notes/compounds-pipeline.md` — pipeline reproduction guide
- `koine-anki/notes/card-quality-standards.md` — quality rules
- `koine-pimsleur/notes/lessons-learned-koine.md` — TTS, contamination, Pimsleur method
- `koine-pimsleur/notes/lessons-learned-replication.md` — replication guide
- Direct file inspection of all source code and data files
