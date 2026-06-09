# Validated Findings: Enhance anki-agent

## Validation Summary

| Section | Status | Notes |
|---------|--------|-------|
| Directory Structure | CONFIRMED (minor gaps) | All 3 subdirs exist as described |
| Deck Generation Tools | CONFIRMED (1 error) | gen_deck.py does NOT use genanki |
| Data Layer (koine-anki/data/) | CONFIRMED (minor inaccuracies) | File sizes/counts slightly off |
| Formats | CONFIRMED (partial errors) | MorphGNT has 7 fields not 6; frequency format differs |
| TTS Rules | CONTRADICTED (code vs KB) | Code strips polytonic; KB says don't strip |
| Vocabulary Targets | CONFIRMED (minor discrepancy) | 600=~90% per README, KB says 85-87% |
| KB Lessons Exist | CONFIRMED | All cited KB entries found |

---

## Section 1: Directory Structure

### `anki-main/` — **CONFIRMED**
- ✅ `languages/` exists with `src/`, `data/`, `audio/` subdirs
- ✅ `SAW/` exists with `.apkg` decks (SAW__Workshop.apkg, SAW_Topics4-9.apkg)
- ✅ `DVA-C02_Questions.txt` exists (57,994 bytes)

### `koine-anki/` — **CONFIRMED**
- ✅ `compounds/` exists with all 5 pipeline scripts
- ✅ `terminaciones/` exists with gen_deck.py, gen_deck_vol3.py, cards_cat1-7.py, cards_vol3_cat1-7.py
- ✅ `data/` exists with all claimed files
- ✅ `decks/` exists
- ✅ `notes/` exists with: compounds-pipeline.md, koine-greek-anki-guidelines.md, card-quality-standards.md

### `koine-pimsleur/` — **CONFIRMED**
- ✅ `src/` exists with engine.py, tts.py, generate.py, render.py, script_builder.py, enrich.py, generate_decks.py
- ✅ `src/data/` has 19 lesson data files covering lessons 1-90
- ✅ `audio/` has 3 levels (level1_el_extranjero, level2_el_discipulo, level3_el_predicador)
- ✅ `decks/` exists
- ✅ `notes/` exists with: curriculum_overview.md, lessons-learned-koine.md, lessons-learned-replication.md, + others

---

## Section 2: Deck Generation Tools

### Tool Table — **CONFIRMED with 1 error**

| Claim | Status | Evidence |
|-------|--------|----------|
| `generate_deck.py` uses genanki → .apkg | ✅ CONFIRMED | `import genanki` found; outputs `decks/matthew_compounds.apkg` |
| `gen_deck.py` → text export | ✅ CONFIRMED | Writes to `greek_infinitives_anki.txt` (tab-separated) |
| `gen_deck_vol3.py` uses genanki → .apkg | ✅ CONFIRMED | `import genanki` found |
| `generate_decks.py` uses genanki → .apkg | ✅ CONFIRMED | `import genanki` found; "4 cards per lesson" in docstring |
| **"All use genanki library"** | ❌ CONTRADICTED | `gen_deck.py` does NOT use genanki — it only uses `importlib` and writes plain text |

### Compounds Pipeline (5 steps) — **CONFIRMED**
- ✅ `extract_compounds.py` — exists (2,900 bytes)
- ✅ `fetch_strongs.py` — exists (4,187 bytes)
- ✅ `enrich_compounds.py` — exists (12,916 bytes), contains SUFFIX_DB and ROOT_CHANGES
- ✅ `improve_mnemonics.py` — exists (18,022 bytes)
- ✅ `generate_deck.py` — exists (8,067 bytes)

### Anti-Duplication System — **CONFIRMED**
- ✅ `compounds_registry.json` exists with 290 entries
- ✅ Format: `{lemma: {source_book, deck, date_added}}` — verified (e.g., `"διαβλέπω": {"source_book": "matthew", "deck": "matthew_compounds", "date_added": "2026-04-03"}`)

### "290 compound word flashcards" — **CONFIRMED**
- ✅ Registry has exactly 290 entries

---

## Section 3: Data Layer (koine-anki/data/)

| File | Claim | Status | Evidence |
|------|-------|--------|----------|
| `nt-morphgnt/` (27 files) | 27 NT books | ✅ CONFIRMED | `ls | wc -l` = 27 |
| `strongs_greek.xml` (2.3MB, 5516 entries) | Size + count | ⚠️ PARTIALLY CONFIRMED | Size = 2.37MB ✅; Entries = **5624** not 5516 ❌ |
| `nt_vocabulary_frequency.json` | `[{rank, lemma, count, pos}]` | ⚠️ PARTIALLY CONFIRMED | Actual format: `{lemma, count, pos, pct}` — has `pct` not `rank` |
| `nt_top600.json` (top 600) | Same format, top 600 | ✅ CONFIRMED | Format: `{rank, lemma, count, pos}`, count = 600 |
| `compounds_registry.json` | Anti-duplication registry | ✅ CONFIRMED | 290 entries, correct format |
| `nt_compounds_full.json` (2.2MB) | Full compound data | ✅ CONFIRMED | Size = 2.25MB |
| `matthew/compounds_enriched.json` | Enriched card data | ⚠️ PARTIALLY CONFIRMED | Exists but keys differ from claim (see below) |
| `es_rvr.json` | Spanish Bible (RVR60) | ✅ CONFIRMED | Exists (4.03MB) |
| `morphology_reference.md` | Suffix/prefix tables | ✅ CONFIRMED | Exists (12.8KB) |
| `morphology_context.md` | Extended morphology | ✅ CONFIRMED | Exists (22.7KB) |
| `nt_grammar_stats.json` | Grammar statistics | ✅ CONFIRMED | Exists (4.1KB) |
| `pronunciation.csv` | Pronunciation guide | ✅ CONFIRMED | Exists (1.0KB) |

### `matthew/compounds_enriched.json` format discrepancy:
- **Claimed keys**: lemma, components[], meaning_es, mnemonic_es, strongs_number, strongs_derivation, strongs_definition, suffix, suffix_type_es, suffix_explanation_es, root_note_es, cognates_by_part, verses[]
- **Actual keys**: `['lemma', 'components', 'meaning_es', 'mnemonic_es', 'first_ref', 'pos', 'strongs_number', 'strongs_derivation', 'strongs_definition', 'cognates', 'cognates_by_part', 'greek_verses']`
- **Missing from actual**: suffix, suffix_type_es, suffix_explanation_es, root_note_es (these are added by `enrich_compounds.py` but not present in the stored file)
- **Missing from claim**: first_ref, pos, cognates, greek_verses

### Cross-project dependency — **CONFIRMED**
- ✅ `koine-pimsleur/src/enrich.py` line 6: `ANKI_REPO = os.environ.get('KOINE_ANKI_PATH', os.path.join(os.path.dirname(__file__), '..', '..', 'koine-anki'))`

---

## Section 4: Formats

### MorphGNT Format — **PARTIALLY CONFIRMED**
- Claim: "Space-delimited: `ref POS morph-code word normalized lemma`" (6 fields)
- Actual: **7 fields** — `ref POS morph-code text word normalized lemma`
- Example: `010101 N- ----NSF- Βίβλος Βίβλος βίβλος βίβλος`
- The claim's own example shows 7 tokens but describes only 6. Standard MorphGNT has: bcv, pos, parsing, text, word, normalized, lemma.

### Frequency list format — **PARTIALLY CONFIRMED**
- `nt_vocabulary_frequency.json`: actual format is `{lemma, count, pos, pct}` (no `rank` field)
- `nt_top600.json`: format IS `{rank, lemma, count, pos}` as claimed

### Lesson data format — **PARTIALLY CONFIRMED**
- Claimed: `{num, intro_es, dialogue, vocab[{gr, es}], phrases[{gr, es}], verse{gr, explain_es}, closing_es}`
- Actual keys: `num, intro_es, dialogue, context_es, vocab, phrases, recon, verse, closing_es`
- Missing from claim: `context_es`, `recon`
- The claimed keys that ARE present are correct in structure

### Card HTML Structure — **CONFIRMED**
- ✅ Front: Greek word (36px) + "¿De qué se compone esta palabra?"
- ✅ Back structure: Word → Meaning (green) → Ref + Strong's → Components → Suffix box → Root-change box → Mnemonic → Cognates → Verses
- Verified from `generate_deck.py` `build_back()` function

---

## Section 5: TTS Rules

### Google Cloud TTS Chirp3-HD (el-GR) — **CONFIRMED**
- ✅ Code uses `el-GR-Chirp3-HD-Achird` (M) and `el-GR-Chirp3-HD-Zephyr` (F)

### Wavenet-B as fallback — **CONTRADICTED in code, CONFIRMED in README**
- ❌ Code (`tts.py`) uses only Chirp3-HD voices as fallbacks: Charon, Aoede, Zephyr, Kore, Achird
- ✅ README states "Chirp3-HD + Wavenet-B fallback"
- **Verdict**: README is outdated or aspirational; actual code does NOT use Wavenet-B

### Amazon Polly (Mia, es-MX, neural) — **CONFIRMED**
- ✅ `tts.py` line 65: `def es(text, voice="Mia", engine="neural")`
- ✅ `tts.py` line 69: `LanguageCode="es-MX"`

### "Pass original polytonic text — do NOT strip to monotonic" — **CONTRADICTED by current code**
- ❌ `tts.py` line 76: `mono = to_mono(text)` — code DOES strip polytonic to monotonic
- ✅ KB lesson confirms this is a KNOWN BUG: "The to_mono() stripping was unnecessary and harmful for short words"
- **Verdict**: The finding states the CORRECT recommendation (from KB), but the code has NOT been fixed. The finding is a prescriptive rule, not a description of current behavior.

### Short word threshold (< 400ms = TTS failure) — **CONFIRMED**
- ✅ `tts.py` line 49: `return max(400, min(n, 4) * 150 + max(0, n - 4) * 80)` — 400ms minimum duration

---

## Section 6: Vocabulary Targets

| Claim | Status | Evidence |
|-------|--------|----------|
| 310 NT words = 80% coverage | ⚠️ UNVERIFIED | KB says "317 = 80%" (jktauber.com). Minor discrepancy (310 vs 317) |
| 600 NT words = ~90% coverage | ⚠️ CONFLICTING | README says ~90% ✅; KB lesson says "85-87% (NOT 90%)" ❌ |
| 882 words = 90% per Lanier 2015 | ✅ CONFIRMED | KB lesson confirms: "882 = 90% per Lanier 2015" |
| Source: jktauber.com frequency data | ✅ CONFIRMED | KB cites jktauber.com |

---

## Section 7: KB Lessons Cited

| Cited Lesson | Status | Evidence |
|--------------|--------|----------|
| "Koine Greek morphology for Anki flashcard design" | ✅ CONFIRMED | Found in KB with matching content |
| "Pimsleur Method for Ancient Language Audio Courses" | ✅ CONFIRMED | Found in KB with matching content |
| "Google Cloud TTS silent audio from polytonic Greek" | ✅ CONFIRMED | Found in KB with matching content |
| "Koine Greek vs Modern Greek: Contamination Prevention" | ✅ CONFIRMED | Found in KB with matching content |
| "Audio-First Language Curriculum Design: Koine Greek" | ✅ CONFIRMED | Found in KB with matching content |

---

## Section 8: Morphology & Anti-Contamination Rules

### SUFFIX_DB entries — **CONFIRMED**
- ✅ 11 entries: τός, σις, μα, ία, εια, μός, ή, ικός, ιος, ών, τής
- Matches claim exactly (claim lists: -τός, -σις, -μα, -ία, -μός, -ή, -ικός, -ιος, -ών, -τής, -εια)

### ROOT_CHANGES (45 words) — **CONFIRMED**
- ✅ Exactly 45 entries found in `enrich_compounds.py`

### Ablaut mappings — **CONFIRMED** (from KB)
- ✅ KB confirms: βάλλω→βολ-, τίθημι→θε-/θη-, ἵστημι→στα-, στέλλω→στολ-

### Anti-contamination checklist — **CONFIRMED** (from KB)
- ✅ KB "Koine Greek vs Modern Greek" lesson confirms all items: no δεν/μην, no θα, no να+subjunctive replacing infinitive, no σε+accusative for dative, no post-Koine vocabulary

---

## Section 9: Pimsleur Course Details

| Claim | Status | Evidence |
|-------|--------|----------|
| 90 lessons | ✅ CONFIRMED | `data/__init__.py` imports L1-L90; ALL_LESSONS has 90 entries |
| 16.7 hours | ✅ CONFIRMED | README states "16.7 hours" |
| ~600 words | ✅ CONFIRMED | README states "~600 Koine Greek words" |
| ~90% NT coverage | ✅ CONFIRMED (per README) | README states "~90% of the NT text" |
| 3 levels × 30 lessons | ✅ CONFIRMED | Audio: 31+30+30 = 91 MP3s across 3 level dirs |
| 4 cards/lesson in generate_decks.py | ✅ CONFIRMED | Docstring: "4 cards per lesson" (2 vocab + 1 phrase + 1 verse, each with recognition+production templates) |

---

## Critical Errors Found

1. **"All use genanki"** — FALSE. `gen_deck.py` (terminaciones Vol. 2) writes plain text, not .apkg.
2. **Strong's entries = 5516** — FALSE. Actual count = 5624.
3. **"Pass original polytonic text"** — CONTRADICTED by current code (code strips to monotonic). This is a known bug per KB but the code hasn't been fixed.
4. **Wavenet-B fallback** — NOT in code. Only Chirp3-HD voices used as fallbacks. README mentions it but code doesn't implement it.
5. **MorphGNT = 6 fields** — FALSE. Actual format has 7 space-delimited fields.
6. **nt_vocabulary_frequency.json format** — WRONG. Has `{lemma, count, pos, pct}` not `{rank, lemma, count, pos}`.
7. **600 words = ~90% NT** — CONFLICTING. README says ~90%, KB lesson says 85-87%.
8. **matthew/compounds_enriched.json fields** — PARTIALLY WRONG. Missing fields (suffix, root_note) and has unlisted fields (first_ref, pos, cognates, greek_verses).

---

## Overall Assessment

The findings are **substantially correct** (~85% accurate) with good coverage of the project structure, tools, and knowledge base. The errors are mostly minor (off-by-one counts, incomplete field lists, format details). The most significant issue is the TTS polytonic claim which describes the *desired* behavior (from KB lessons learned) rather than the *actual* code behavior — this is important context for the enhanced prompt since it represents a known unfixed bug.
