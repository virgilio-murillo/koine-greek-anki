# Investigation Findings: Enhance anki-agent

## Source: Knowledge Base + Lessons Learned + Filesystem Analysis

---

## 1. What's in Each Subdirectory

### `anki-main/`
The **original monorepo** (now superseded by the split repos below). Contains:
- `languages/` — Combined Anki deck + Pimsleur audio course (all src/ scripts, data/, audio/)
- `SAW/` — AWS Solutions Architect Workshop .apkg decks (unrelated to Greek)
- `DVA-C02_Questions.txt` — AWS Developer Associate exam questions

### `koine-anki/` (ACTIVE — Flashcard Decks)
Koine Greek Anki flashcard generation. Two deck types:
- **`compounds/`** — 290 compound word flashcards with etymological decomposition pipeline
  - Pipeline: `extract_compounds.py` → `fetch_strongs.py` → `enrich_compounds.py` → `improve_mnemonics.py` → `generate_deck.py`
- **`terminaciones/`** — Grammar endings flashcards (verb conjugations, infinitives, participles)
  - `gen_deck.py` (Vol. 2 — text export), `gen_deck_vol3.py` (Vol. 3 — .apkg)
  - 7 category files (`cards_cat1.py` through `cards_cat7.py` + vol3 variants)
- **`data/`** — NT corpus and linguistic reference data (shared with koine-pimsleur)
- **`decks/`** — Generated .apkg output files
- **`notes/`** — Guidelines, pipeline docs, quality standards

### `koine-pimsleur/` (ACTIVE — Audio Course)
90-lesson Pimsleur-style audio course (16.7 hours, ~600 words, ~90% NT coverage):
- **`src/`** — Generation engine: `engine.py`, `tts.py`, `generate.py`, `render.py`, `script_builder.py`, `enrich.py`, `generate_decks.py`
- **`src/data/`** — 90 lesson content files (Python modules with vocab, phrases, dialogues)
- **`audio/`** — Generated MP3s organized by level (3 levels × 30 lessons)
- **`decks/`** — Generated lesson MP3s + Anki decks from lessons
- **`notes/`** — Curriculum design, lessons learned, replication guide

---

## 2. Deck Generation Tools

| Tool | Location | Purpose | Output |
|------|----------|---------|--------|
| `generate_deck.py` | `koine-anki/compounds/` | Compound word flashcards from enriched JSON | `.apkg` (HTML cards) |
| `gen_deck.py` | `koine-anki/terminaciones/` | Grammar endings Vol. 2 | Text export |
| `gen_deck_vol3.py` | `koine-anki/terminaciones/` | Grammar endings Vol. 3 | `.apkg` |
| `generate_decks.py` | `koine-pimsleur/src/` | Anki decks from Pimsleur lessons (4 cards/lesson) | `.apkg` |

**All use `genanki` library** with stable model/deck IDs. Card styling uses inline HTML+CSS.

### Compounds Pipeline (5 steps):
1. `extract_compounds.py` — Extract compound candidates from MorphGNT using prefix list
2. `fetch_strongs.py` — Add Strong's etymology for compound + components
3. `enrich_compounds.py` — Add suffix explanations + root-change notes (built-in SUFFIX_DB + ROOT_CHANGES)
4. `improve_mnemonics.py` — Replace short mnemonics with full explanations (LLM step)
5. `generate_deck.py` — Create .apkg with styled HTML cards

### Anti-Duplication System:
`data/compounds_registry.json` maps each processed lemma to its source book. When processing new books, filter out already-registered lemmas.

---

## 3. Relationship to bible-tools / koine-anki/data/

`koine-anki/data/` is the **shared data layer** consumed by both projects:

| File | Format | Purpose |
|------|--------|---------|
| `nt-morphgnt/` (27 files) | Space-delimited: `ref POS morph-code word normalized lemma` | Full NT morphologically tagged |
| `strongs_greek.xml` | XML (2.3MB) | Strong's Greek Dictionary — 5516 entries |
| `nt_vocabulary_frequency.json` | `[{rank, lemma, count, pos}]` | Word frequency list |
| `nt_top600.json` | Same format, top 600 | Core vocabulary (~90% NT coverage) |
| `compounds_registry.json` | `{lemma: {source_book, deck, date_added}}` | Anti-duplication registry |
| `nt_compounds_full.json` | Full compound data (2.2MB) | All NT compounds enriched |
| `matthew/compounds_enriched.json` | Full card data with components, strongs, suffix, root_note, mnemonic, cognates, verses | Matthew deck source |
| `es_rvr.json` | Spanish Bible (RVR60) | Spanish verse translations |
| `morphology_reference.md` | Markdown | Suffix/prefix reference tables |
| `morphology_context.md` | Markdown | Extended morphology context |
| `nt_grammar_stats.json` | JSON | Grammar statistics |
| `pronunciation.csv` | CSV | Pronunciation guide |

**Cross-project dependency**: `koine-pimsleur` references `koine-anki/data/` via `KOINE_ANKI_PATH` env var (or sibling directory detection) for enriching lesson scripts with NT vocabulary and morphology data.

---

## 4. Formats Used

### Data Formats:
- **MorphGNT**: Space-delimited text (`010101 N- ----NSF- Βίβλος Βίβλος βίβλος βίβλος`)
- **Frequency lists**: JSON arrays of `{rank, lemma, count, pos}`
- **Compounds registry**: JSON object `{lemma: {source_book, deck, date_added}}`
- **Enriched compounds**: JSON with `{lemma, components[], meaning_es, mnemonic_es, strongs_number, strongs_derivation, strongs_definition, suffix, suffix_type_es, suffix_explanation_es, root_note_es, cognates_by_part, verses[]}`
- **Lesson data**: Python modules exporting `LESSONS` list of `{num, intro_es, dialogue, vocab[{gr, es}], phrases[{gr, es}], verse{gr, explain_es}, closing_es}`
- **Strong's**: XML

### Output Formats:
- `.apkg` — Anki package (zip containing SQLite + media)
- `.mp3` — Audio lessons
- `.txt` — Text exports (terminaciones)

### Card HTML Structure (Compounds):
Front: Greek word + "¿De qué se compone esta palabra?"
Back: Word (36px) → Meaning (green) → Ref + Strong's → Components boxes → Suffix box (purple) → Root-change box (orange) → Mnemonic box (green) → Cognates box (blue) → Verses box (tan)

---

## 5. What the Enhanced Prompt Should Contain

Based on lessons learned (KB), project documentation, and agent scoping best practices:

### Critical Rules Section (highest ROI per shared learnings):
1. **Greek text MUST use NFC normalization** — polytonic Unicode must be normalized
2. **Never strip polytonic diacritics** — Google TTS handles them correctly; stripping causes silent audio for short words
3. **Never use Modern Greek vocabulary/grammar** — use Koine forms only (ὕδωρ not νερό, οἶκος not σπίτι, dative case not σε+accusative)
4. **Cards must be 100% self-contained** — every morpheme explained
5. **Verify all Greek against NT corpus** — use MorphGNT data, not assumptions
6. **All explanations in Spanish** — user is native Spanish speaker

### Project Context:
- Three subdirectories: `anki-main/` (legacy), `koine-anki/` (flashcards), `koine-pimsleur/` (audio)
- Shared data in `koine-anki/data/` (MorphGNT, Strong's, frequency lists)
- All deck generation uses `genanki` library with stable IDs
- Python 3.12+ environment with venv

### Pipeline Knowledge:
- Compounds pipeline: extract → fetch_strongs → enrich → improve_mnemonics → generate_deck
- Anti-duplication via `compounds_registry.json`
- Terminaciones: category files → gen_deck_vol3.py
- Pimsleur: lesson data modules → generate_decks.py (4 cards/lesson, recognition + production)

### Morphology Rules (from lessons learned):
- 3-layer annotation: suffix meaning, root-change explanation, prefix allomorph note
- Key ablaut mappings: βάλλω→βολ-, τίθημι→θε-/θη-, ἵστημι→στα-, στέλλω→στολ-
- Prefix assimilation: elision, aspiration (π/τ/κ→φ/θ/χ), nasal assimilation
- Beginner cards: max 3-4 elements, no ablaut terminology, use English cognate anchors

### TTS Rules (from lessons learned):
- Google Cloud TTS Chirp3-HD (el-GR) for Greek speech
- Wavenet-B as fallback for short words (< 400ms = TTS failure)
- Amazon Polly (Mia, es-MX, neural) for Spanish narration
- Pass original polytonic text — do NOT strip to monotonic

### Anti-Contamination Checklist:
- No δεν/μην (use οὐ/μή)
- No θα (use synthetic future -σω)
- No να+subjunctive where infinitive goes
- No σε+accusative for indirect objects (use dative)
- No post-Koine vocabulary (νερό, σπίτι, ψωμί, πόρτα)

### Card Quality Standards:
- Mnemonics must be >40 chars and explain WHY (not just translate)
- Include Strong's data for compound AND each component
- Suffix explanations for all suffixed words (SUFFIX_DB: -τός, -σις, -μα, -ία, -μός, -ή, -ικός, -ιος, -ών, -τής, -εια)
- Root-change notes for all affected words (ROOT_CHANGES: 45 words)
- Biblical references when relevant
- Spanish/English cognates when available

### Vocabulary Targets:
- 310 NT words = 80% coverage
- 600 NT words = ~90% coverage (target for 90-lesson course)
- 882 words = 90% per Lanier 2015
- Source: jktauber.com frequency data

---

## Sources
- `koine-anki/README.md`, `koine-pimsleur/README.md`, `anki-main/languages/README.md`
- `koine-anki/notes/compounds-pipeline.md`
- `koine-anki/notes/koine-greek-anki-guidelines.md`
- `koine-anki/notes/card-quality-standards.md`
- `koine-pimsleur/notes/curriculum_overview.md`
- `koine-pimsleur/notes/lessons-learned-koine.md`
- `koine-pimsleur/notes/lessons-learned-replication.md`
- Lessons Learned KB: "Koine Greek morphology for Anki flashcard design"
- Lessons Learned KB: "Pimsleur Method for Ancient Language Audio Courses"
- Lessons Learned KB: "Google Cloud TTS silent audio from polytonic Greek"
- Lessons Learned KB: "Koine Greek vs Modern Greek: Contamination Prevention"
- Lessons Learned KB: "Audio-First Language Curriculum Design: Koine Greek"
- Filesystem analysis of all three subdirectories
