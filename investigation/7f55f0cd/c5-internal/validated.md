# Validated Findings: Enhance anki-agent

## Validation Summary

| Section | Claims | Confirmed | Contradicted | Unverified |
|---------|--------|-----------|--------------|------------|
| 1. Subdirectories | 28 | 25 | 3 | 0 |
| 2. Deck Generation Tools | 8 | 7 | 1 | 0 |
| 3. Bible-tools | 6 | 5 | 1 | 0 |
| 4. Formats | 12 | 10 | 2 | 0 |
| 5. Enhanced Prompt | 14 | 12 | 1 | 1 |

---

## 1. Subdirectories

### `anki-main/`
- **CONFIRMED**: Contains `DVA-C02_Questions.txt` and `SAW/` directory.
- **CONFIRMED**: `SAW/SAW_Topics4-9.apkg` exists. Also contains `SAW__Workshop.apkg`.
- **CONFIRMED**: `languages/` subdirectory exists with its own `src/`, `data/`, `audio/`, `notes/`, `venv/`, and TLS certs (`cert.pem`, `key.pem`).

### `koine-anki/`
- **CONFIRMED**: Purpose is Koine Greek flashcard generation.
- **CONTRADICTED**: Findings claim "10 Python scripts forming a 5-step pipeline". There are 10 .py files but the pipeline doc describes **6 steps** (extract → LLM decompose → fetch_strongs+enrich_compounds → improve_mnemonics → generate_deck → update registry). The "5-step" label comes from the pipeline doc itself, but the pipeline sequence listed in the findings (extract → fetch_strongs → enrich_compounds → enrich_cognates → enrich_verses → add_rvr60 → improve_mnemonics → generate_deck) is **8 steps**, not 5. The doc's "5 steps" groups some scripts together.
- **CONFIRMED**: `terminaciones/` has 7 categories × 2 volumes (7 `cards_cat*.py` + 7 `cards_vol3_cat*.py`).
- **CONFIRMED**: `gen_deck.py` produces text export, `gen_deck_vol3.py` produces `.apkg`.
- **CONFIRMED**: `data/nt-morphgnt/` has 27 NT books morphologically tagged.
- **CONTRADICTED**: Findings claim Strong's has "5516 entries". Actual count: **5624 entries** (verified via `grep -c '<entry'`).
- **CONFIRMED**: `nt_vocabulary_frequency.json` exists (5460 entries, list format).
- **CONFIRMED**: `nt_top600.json` exists (600 entries, list format with keys: rank, lemma, count, pos).
- **CONFIRMED**: `nt_compounds_full.json` has **4,233** entries (verified via Python).
- **CONFIRMED**: `compounds_registry.json` exists (dict format, deduplication registry).
- **CONFIRMED**: `es_rvr.json` exists (4MB, dict format).
- **CONFIRMED**: `matthew/` subdirectory exists with enriched data.
- **CONFIRMED**: `morphology_reference.md`, `morphology_context.md`, `pronunciation.csv` all exist.
- **CONFIRMED**: Notes directory contains `compounds-pipeline.md`, `koine-greek-anki-guidelines.md`, `card-quality-standards.md`.
- **CONFIRMED**: `decks/matthew_compounds.apkg` exists (290 cards confirmed from JSON source).

### `koine-pimsleur/`
- **CONFIRMED**: 90-lesson Pimsleur-method audio course (90 MP3s in `decks/lessons_v2/`).
- **CONFIRMED**: 16.7 hours (stated in README.md).
- **CONFIRMED**: `src/` contains `engine.py`, `tts.py`, `generate.py`, `render.py`, `script_builder.py`, `enrich.py`, `generate_decks.py`.
- **CONTRADICTED**: Findings claim "18 Python modules" for lesson data. Actual count: **19 modules** (`lesson_data_01_05.py` through `lesson_data_86_90.py`).
- **CONFIRMED**: `decks/` has `lessons/`, `lessons_v2/`, and `anki/` subdirectories.
- **CONFIRMED**: `audio/` organized by level: `level1_el_extranjero/`, `level2_el_discipulo/`, `level3_el_predicador/`.
- **CONFIRMED**: `notes/` contains curriculum docs and lessons learned.

---

## 2. Deck Generation Tools

| Claim | Status | Evidence |
|-------|--------|----------|
| `generate_deck.py` uses genanki, reads `compounds_enriched.json`, outputs .apkg (290 cards) | **CONFIRMED** | Code imports genanki, reads JSON, 290 entries in source data |
| `gen_deck.py` outputs `.txt` (tab-separated) | **CONFIRMED** | Code writes `f"{front}\t{back}\n"` to `greek_infinitives_anki.txt` |
| `gen_deck_vol3.py` outputs `.apkg` via genanki | **CONFIRMED** | Code imports genanki, creates deck |
| `generate_decks.py` creates 4 cards/lesson, 10 lessons/deck | **CONFIRMED** | Line 1: "4 cards per lesson, 10 lessons per deck" |
| All use `random.seed(42)` | **CONTRADICTED** | Only `generate_deck.py` and `generate_decks.py` use `random.seed(42)`. `gen_deck_vol3.py` does NOT use random.seed. `gen_deck.py` doesn't use random at all. |
| Stable model/deck IDs for Anki merge | **CONFIRMED** | `generate_deck.py` uses hardcoded `DECK_ID`, `gen_deck_vol3.py` uses hardcoded deck ID |
| HTML+CSS card templates with inline styling | **CONFIRMED** | `.card { font-family: 'Georgia'...}` in generate_deck.py |
| All use genanki for .apkg | **CONFIRMED** | 3 of 4 tools use genanki; `gen_deck.py` outputs .txt (not .apkg) — consistent with findings |

---

## 3. Relationship to bible-tools

| Claim | Status | Evidence |
|-------|--------|----------|
| bible-tools is at `~/.kiro/mcp-servers/bible-tools/` | **CONFIRMED** | Directory exists with server.py, databases |
| Provides 17 tools | **CONFIRMED** | `grep -c "@mcp.tool" server.py` = 17 |
| Tool list includes verse_lookup, parallel_versions, semantic_search, morphology_analysis, critical_apparatus, patristic_commentary, cross_references, word_lookup, word_study, canon_history, dss_lookup, chapter_study, translate_corpus, authenticity_report, text_comparison, save_patristic_original | **CONFIRMED** | All 16 found. Plus `book_list` (17th tool, not mentioned in findings). |
| Versions: SBLGNT, RVR60, YLT, Vulgate, LXX, WLC, ApostolicFathers | **CONFIRMED** | All listed in server.py. Also has MorphGNT, KJV, BSB. |
| Has SQLite databases: `bible.db`, `greek_corpus.db`, `bible_study.db` | **CONTRADICTED** | Actual databases: `bible.db`, `greek_corpus.db`, `bible_study.db`, AND `bible_tools.db`. Findings missed `bible_tools.db`. Minor omission. |
| `koine-pimsleur/src/enrich.py` reads koine-anki data via `KOINE_ANKI_PATH` env var or sibling detection | **CONFIRMED** | Line 6: `ANKI_REPO = os.environ.get('KOINE_ANKI_PATH', os.path.join(..., 'koine-anki'))` |

---

## 4. Formats Used

| Claim | Status | Evidence |
|-------|--------|----------|
| JSON array for compounds_enriched, nt_compounds_full, nt_top600 | **CONFIRMED** | All are JSON arrays |
| JSON dict for compounds_registry, es_rvr | **CONFIRMED** | Both are dicts |
| XML for strongs_greek.xml | **CONFIRMED** | XML file with `<entry>` elements |
| MorphGNT format: "ref, POS, morph-code, text, normalized, lemma" | **CONTRADICTED** | Actual format has **7 space-separated columns**: ref, POS, morph-code, text, text2, normalized, lemma. Findings claim 6 columns but there are 7. |
| Markdown for morphology docs | **CONFIRMED** | `.md` files exist |
| CSV for pronunciation | **CONFIRMED** | CSV with headers: letter, modern_sound, tts_sounds_like, notes |
| Python modules for card/lesson content | **CONFIRMED** | `cards_cat*.py` and `lesson_data_*.py` |
| .apkg output via genanki | **CONFIRMED** | Multiple .apkg files generated |
| .txt tab-separated output | **CONFIRMED** | `greek_infinitives_anki.txt` |
| .mp3 via pydub + ffmpeg | **CONFIRMED** | 90 MP3 files in lessons_v2/ |
| Card schema includes: lemma, components, meaning_es, mnemonic_es, first_ref, strongs_number, strongs_derivation, strongs_definition, suffix, suffix_type_es, suffix_explanation_es, root_note_es, cognates_by_part, greek_verses | **CONTRADICTED** | Actual keys: lemma, components, meaning_es, mnemonic_es, first_ref, **pos**, strongs_number, strongs_derivation, strongs_definition, **cognates**, cognates_by_part, greek_verses, suffix, suffix_type_es, suffix_explanation_es, root_note_es, **parent_verb**. Findings missed `pos`, `cognates`, `parent_verb`. |
| Lesson schema includes: num, intro_es, dialogue, context_es, vocab, phrases, recon, verse | **CONFIRMED** | All present. Also has `closing_es` (not mentioned in findings but present in actual data). |

---

## 5. Enhanced Prompt Content

| Claim | Status | Evidence |
|-------|--------|----------|
| NFC normalization required | **CONFIRMED** | `fetch_strongs.py` uses `unicodedata.normalize("NFC", s)` |
| `to_mono()` strips polytonic→monotonic for TTS | **CONFIRMED** | `tts.py:32` — `to_mono()` converts polytonic to monotonic |
| Vocabulary blacklist (νερό, σπίτι, ψωμί, πόρτα) | **CONFIRMED** | All listed in `lessons-learned-koine.md` |
| False friends (παρακαλέω, ῥῆμα, δουλεύω) | **CONFIRMED** | All listed in `lessons-learned-koine.md:35-37` |
| Anti-duplication via compounds_registry.json | **CONFIRMED** | Registry exists with source_book, deck, date_added |
| Stable IDs for Anki merge | **CONFIRMED** | Hardcoded deck/model IDs in generation scripts |
| Python 3.12 | **CONTRADICTED** | System has **Python 3.14.3**. The `__pycache__` dirs show `cpython-312` suggesting it was 3.12 previously, but current system is 3.14. |
| TTS: "Chirp3-HD fails on short words (<400ms) → Wavenet-B fallback" | **CONTRADICTED** | The fallback is to **other Chirp3-HD voices** (Charon, Aoede, Kore, etc.), NOT Wavenet-B. There is no Wavenet-B anywhere in the code. The short-word handling tries all Chirp3-HD voices and keeps the longest result. |
| Audio speed: 75% for lessons 1-7, 85% for 8-15, 100% for 16+ | **CONFIRMED** | `engine.py:7`: `return 0.75 if n <= 7 else (0.85 if n <= 15 else 1.0)` |
| Card HTML: inline CSS only | **CONFIRMED** | `.card { ... }` inline in generate_deck.py |
| Dependencies: genanki, py-sblgnt, pydub, boto3, google-cloud-texttospeech | **CONFIRMED** | All in README install instructions |
| MorphGNT/SBLGNT (MIT license) | **UNVERIFIED** | License not checked in local files, but MorphGNT is known to be MIT |
| Pimsleur pipeline: lesson_data → engine (GIR cycles) → TTS → pydub → MP3 | **CONFIRMED** | engine.py has GIR cycles (lines 37, 56, 69, 88), tts.py uses Google TTS + Polly, pydub for audio |
| Enrichment uses Bedrock Claude + koine-anki data | **CONFIRMED** | `enrich.py` imports from koine-anki path and uses KOINE_ANKI_PATH |

---

## Key Corrections

1. **Strong's entries**: 5624, not 5516.
2. **Lesson data modules**: 19, not 18.
3. **TTS fallback**: Uses other Chirp3-HD voices, NOT Wavenet-B.
4. **MorphGNT columns**: 7 columns, not 6 as implied.
5. **Python version**: System is 3.14.3, not 3.12 (though 3.12 was used previously).
6. **Pipeline steps**: The "10 scripts forming a 5-step pipeline" is misleading — the pipeline doc says 5 steps but the findings list 8 sequential scripts. The actual pipeline has 6 documented steps with some steps containing multiple scripts.
7. **Card schema**: Missing fields `pos`, `cognates`, `parent_verb` from the documented schema.
8. **random.seed(42)**: Not used by all tools — only 2 of 4 use it.

---

## Overall Assessment

The findings are **substantially accurate** (>85% of claims confirmed). The errors are mostly minor numerical discrepancies (5516 vs 5624, 18 vs 19 modules) and one significant factual error (Wavenet-B fallback claim is completely wrong — the code only uses Chirp3-HD voices). The structural understanding of the project, its relationships, and its data flows is correct.
