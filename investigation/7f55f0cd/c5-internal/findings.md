# Internal Investigation Findings: Enhance anki-agent

## Source: Local project analysis + internal tool exploration
**Note**: Amazon internal tools (InternalSearch, Atlas, SearchSoftwareRecommendations) were unavailable due to expired Midway credentials. Findings are based on comprehensive local project analysis.

---

## 1. What's in Each Subdirectory

### `anki-main/`
- **Purpose**: Original monorepo (now mostly historical). Contains AWS cert prep (`DVA-C02_Questions.txt`, `SAW/`) and a `languages/` subdirectory that was the precursor to the split repos.
- **`languages/`**: Contains a copy of the Pimsleur + Anki pipeline code (older version). Has its own `src/`, `data/`, `decks/`, `audio/`, `notes/`, `venv/`, and TLS certs for `serve_audio.py`.
- **Key files**: `DVA-C02_Questions.txt` (AWS Developer Associate prep), `SAW/SAW_Topics4-9.apkg` (Solutions Architect Workshop)

### `koine-anki/`
- **Purpose**: Koine Greek Anki flashcard generation — compound words and grammar endings.
- **Subdirectories**:
  - `compounds/` — 10 Python scripts forming a 5-step pipeline: extract → fetch_strongs → enrich_compounds → enrich_cognates → enrich_verses → add_rvr60 → improve_mnemonics → audit_cognates → generate_deck
  - `terminaciones/` — Grammar endings decks (7 categories × 2 volumes). `gen_deck.py` (text export), `gen_deck_vol3.py` (.apkg)
  - `data/` — **Shared data layer** used by both koine-anki and koine-pimsleur:
    - `nt-morphgnt/` — 27 NT books morphologically tagged (MorphGNT/SBLGNT)
    - `strongs_greek.xml` — Strong's Greek Dictionary (5516 entries)
    - `nt_vocabulary_frequency.json` — Word frequencies
    - `nt_top600.json` — Top 600 NT words
    - `nt_compounds_full.json` — 4,233 compound word entries (full NT)
    - `compounds_registry.json` — Deduplication registry
    - `es_rvr.json` — Spanish RVR60 Bible text
    - `matthew/` — Matthew-specific enriched data
    - `morphology_reference.md`, `morphology_context.md` — Grammar references
    - `pronunciation.csv` — Pronunciation guide
  - `notes/` — Guidelines: `compounds-pipeline.md`, `koine-greek-anki-guidelines.md`, `card-quality-standards.md`
  - `decks/` — Generated output: `matthew_compounds.apkg` (290 cards)

### `koine-pimsleur/`
- **Purpose**: 90-lesson Pimsleur-method audio course for Koine Greek (16.7 hours).
- **Subdirectories**:
  - `src/` — Generation pipeline: `engine.py` (audio assembly), `tts.py` (Polly + Google TTS), `generate.py` (lesson generator), `render.py` (MP3 renderer), `script_builder.py`, `enrich.py` (LLM enrichment using koine-anki data), `generate_decks.py` (Anki deck from lessons)
  - `src/data/` — 18 Python modules with structured lesson content (90 lessons total)
  - `decks/` — Generated MP3s (`lessons/`, `lessons_v2/`) and `.apkg` files (`anki/`)
  - `audio/` — Organized by level: `level1_el_extranjero/`, `level2_el_discipulo/`, `level3_el_predicador/`
  - `notes/` — Curriculum docs, lessons learned, project notes

---

## 2. Deck Generation Tools

| Tool | Location | Input | Output | Library |
|------|----------|-------|--------|---------|
| `generate_deck.py` | `koine-anki/compounds/` | `data/matthew/compounds_enriched.json` | `.apkg` (290 cards) | genanki |
| `gen_deck.py` | `koine-anki/terminaciones/` | 7 `cards_cat*.py` modules | `.txt` (tab-separated) | none |
| `gen_deck_vol3.py` | `koine-anki/terminaciones/` | 7 `cards_vol3_cat*.py` modules | `.apkg` | genanki |
| `generate_decks.py` | `koine-pimsleur/src/` | `src/data/ALL_LESSONS` | `.apkg` (4 cards/lesson, 10 lessons/deck) | genanki |

**Common pattern**: All use `genanki` for `.apkg` generation with:
- Stable model IDs and deck IDs (for Anki merge compatibility)
- HTML+CSS card templates with inline styling
- `random.seed(42)` for reproducibility

---

## 3. Relationship to bible-tools

**`bible-tools`** is a separate Kiro MCP server at `~/.kiro/mcp-servers/bible-tools/` providing 17 tools:
- `verse_lookup` (SBLGNT, RVR60, YLT, Vulgate, LXX, WLC, ApostolicFathers)
- `parallel_versions`, `semantic_search`, `morphology_analysis`
- `critical_apparatus`, `patristic_commentary`, `cross_references`
- `word_lookup`, `word_study`, `canon_history`, `dss_lookup`
- `chapter_study`, `translate_corpus`, `authenticity_report`
- `text_comparison`, `save_patristic_original`

**Relationship**: `koine-anki/data/` and `bible-tools` share the same upstream sources (MorphGNT, Strong's, openscriptures) but are independent. `koine-anki/data/` is a curated subset optimized for flashcard generation. `bible-tools` has its own SQLite databases (`bible.db`, `greek_corpus.db`, `bible_study.db`) with broader coverage.

**Integration point**: `koine-pimsleur/src/enrich.py` reads `koine-anki/data/` via `KOINE_ANKI_PATH` env var (or sibling directory detection). The bible-tools MCP server could be used during enrichment for verse lookups and morphology analysis.

---

## 4. Formats Used

### Data Formats
| Format | Files | Purpose |
|--------|-------|---------|
| JSON array | `compounds_enriched.json`, `nt_compounds_full.json`, `nt_top600.json` | Structured card data |
| JSON dict | `compounds_registry.json`, `es_rvr.json` | Lookup maps |
| XML | `strongs_greek.xml` | Strong's dictionary |
| Space-separated text | `nt-morphgnt/*.txt` | MorphGNT corpus (ref, POS, morph-code, text, normalized, lemma) |
| Markdown | `morphology_reference.md`, `morphology_context.md` | Grammar references |
| CSV | `pronunciation.csv` | Pronunciation guide |
| Python modules | `cards_cat*.py`, `lesson_data_*.py` | Card/lesson content as code |

### Output Formats
| Format | Tool | Notes |
|--------|------|-------|
| `.apkg` | genanki | Anki package (zip with SQLite + media) |
| `.txt` | manual | Tab-separated front\tback (Anki import) |
| `.mp3` | pydub + ffmpeg | Audio lessons |

### Card Data Schema (compounds_enriched.json)
```json
{
  "lemma": "ἀποκαλύπτω",
  "components": [{"greek": "ἀπό", "meaning_es": "lejos de", "strongs_number": "G575", "strongs_definition": "..."}],
  "meaning_es": "revelar",
  "mnemonic_es": "...",
  "first_ref": "Mt 10:26",
  "strongs_number": "G601",
  "strongs_derivation": "...",
  "strongs_definition": "...",
  "suffix": "-τω",
  "suffix_type_es": "...",
  "suffix_explanation_es": "...",
  "root_note_es": "...",
  "cognates_by_part": {...},
  "greek_verses": [{"ref": "...", "text": "...", "rvr60": "..."}]
}
```

### Lesson Data Schema (lesson_data_*.py)
```python
{
  "num": 1,
  "intro_es": "...",
  "dialogue": [(M, "Χαῖρε!"), (F, "Εἰρήνη σοι.")],
  "context_es": "...",
  "vocab": [{"gr": "χαῖρε", "es": "hola", "note_es": "..."}],
  "phrases": [{"gr": "...", "es": "...", "prompt_es": "..."}],
  "recon": [{"other_gr": "...", "prompt_es": "...", "answer_gr": "..."}],
  "verse": {"gr": "...", "ref": "...", "explain_es": "..."}
}
```

---

## 5. What the Enhanced Prompt Should Contain

Based on the project's documented guidelines, lessons learned, and shared learnings:

### Critical Rules (highest ROI per shared learnings)
1. **Greek text MUST use NFC normalization** — `unicodedata.normalize('NFC', text)` before any comparison or storage. The `to_mono()` function strips polytonic→monotonic for TTS only.
2. **Verify all Greek against NT/LXX attestation** — No Modern Greek contamination. Check vocabulary blacklist (νερό, σπίτι, ψωμί, πόρτα) and false friends (παρακαλέω, ῥῆμα, δουλεύω).
3. **Cards must be 100% self-contained** — Every morpheme explained (prefix, root, suffix). No external lookups needed.
4. **Mnemonics must tell a story** — Not just translations. Include biblical context, Spanish/English cognates, vivid imagery. Minimum 40 chars.
5. **Anti-duplication**: Check `compounds_registry.json` before processing new books.
6. **Stable IDs**: genanki model/deck IDs must be stable across regenerations for Anki merge compatibility.

### Project Context
- User: Native Spanish speaker, also speaks English. Beginner in Koine Greek.
- All explanations in Spanish. Simplified grammar terminology (no "1ª declinación" → "grupo -η/-α").
- Three complementary learning tools: flashcards (koine-anki), audio course (koine-pimsleur), Bible research (bible-tools MCP).
- Data layer: `koine-anki/data/` is the shared source of truth.

### Pipeline Knowledge
- Compounds pipeline: extract → fetch_strongs → enrich_compounds → enrich_cognates → enrich_verses → add_rvr60 → improve_mnemonics → generate_deck
- Pimsleur pipeline: lesson_data → engine (GIR cycles) → TTS (Polly+Google) → pydub → MP3
- Enrichment: `src/enrich.py` uses Bedrock Claude + koine-anki data

### Technical Constraints
- Python 3.12, genanki, py-sblgnt, pydub, boto3, google-cloud-texttospeech
- TTS: Chirp3-HD fails on short words (<400ms) → Wavenet-B fallback
- Audio: 75% speed for lessons 1-7, 85% for 8-15, 100% for 16+
- Card HTML: inline CSS only (Anki renders HTML, no external stylesheets)

### Data Sources Available
- MorphGNT/SBLGNT (MIT) — NT text with lemmas + morphology
- Strong's Greek Dictionary (public domain) — Etymology for 5516 words
- openscriptures/LxxLemmas (Open) — Septuagint lemmatized
- RVR60 Spanish Bible — For verse translations
- bible-tools MCP server — 17 tools for verse lookup, morphology, cross-references, patristic commentary

### Quality Standards
- Suffix explanations for all -τός, -σις, -μα, -ία, -μός, -ή, -ικός, -ιος, -ών, -τής, -εια suffixes
- Root-change notes for 45+ words where verb roots change form (βάλλω→βολ-, τίθημι→θε-/θηκ-)
- Contrastive explanations showing alternatives ("Termina en X porque... Si fuera Y significaría...")
- Strong's data for compound AND each component

---

## Internal Source Limitations

All Amazon internal tools (InternalSearch, Atlas, BuilderHub, Sage, TicketingReadActions, SearchSoftwareRecommendations) returned Midway authentication errors. The findings above are based entirely on local project file analysis, which proved sufficient given this is a personal project with comprehensive local documentation.
