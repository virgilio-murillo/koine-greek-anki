# Validated Findings

## Section 1: Directory Structure

| Claim | Verdict | Evidence |
|-------|---------|----------|
| `anki-main/` exists with SAW/, DVA-C02_Questions.txt, languages/ | **CONFIRMED** | `ls anki-main/` shows exactly these items |
| `anki-main/` has venv/, src/, data/, decks/, notes/, audio/ | **CONFIRMED** | These exist inside `anki-main/languages/` (not at anki-main root) |
| `koine-anki/` has compounds/, terminaciones/, data/, notes/, decks/, kiro-test/ | **CONFIRMED** | Directory listing confirms all |
| `koine-pimsleur/` has src/, audio/, decks/, notes/, serve_audio.py | **CONFIRMED** | Directory listing confirms all |

## Section 2: Compounds Pipeline

| Claim | Verdict | Evidence |
|-------|---------|----------|
| 8-step pipeline: extract → fetch_strongs → enrich_compounds → enrich_cognates → enrich_verses → add_rvr60 → improve_mnemonics → generate_deck | **CONFIRMED** | All 8 scripts exist in `koine-anki/compounds/`. Note: the `compounds-pipeline.md` doc only describes 5 steps (the doc is outdated); enrich_cognates, enrich_verses, and add_rvr60 were added later |
| `audit_cognates.py` exists for quality checks | **CONFIRMED** | File exists (11,349 bytes) |
| `generate_deck.py` uses genanki | **CONFIRMED** | Code imports genanki |
| `gen_deck.py` outputs TSV text | **CONFIRMED** | Writes tab-separated front/back to `greek_infinitives_anki.txt` |
| `gen_deck_vol3.py` uses genanki for .apkg | **CONFIRMED** | Code imports genanki, writes .apkg |
| `generate_decks.py` (pimsleur) creates 4 cards/lesson | **CONFIRMED** | Docstring says "4 cards per lesson", code picks 4 cards per lesson |

## Section 3: Data Files

| Claim | Verdict | Evidence |
|-------|---------|----------|
| Matthew compounds: 290 entries | **CONFIRMED** | `len(json.load(...))` = 290 |
| Full NT+LXX compounds: 4,233 entries | **CONFIRMED** | `len(json.load(...))` = 4233 |
| Top 600 NT words in nt_top600.json | **CONFIRMED** | `len(json.load(...))` = 600 |
| MorphGNT: 27 NT books | **CONFIRMED** | `ls | wc -l` = 27 files |
| Strong's Greek XML: 2.3MB | **CONFIRMED** | 2,369,537 bytes ≈ 2.3MB |
| nt_vocabulary_frequency.json: 506KB | **CONFIRMED** | 506,362 bytes (506KB decimal) |
| es_rvr.json: 4MB | **PARTIALLY CONFIRMED** | 4,031,113 bytes ≈ 3.8MiB / 4.0MB decimal. Close enough |
| es_rvr.json: 66 books, Array of {abbrev, name, chapters[][]} | **CONFIRMED** | JSON is list of 66 items with keys ['abbrev', 'chapters', 'name'] |
| Strong's: "5,516 NT words" | **CONTRADICTED** | Actual count: 5,624 entries. The README says 5516 but the XML has 5624 |
| compounds_registry.json: Map of lemma → {source_book, deck, date_added} | **CONFIRMED** | First entry: `{"source_book": "matthew", "deck": "matthew_compounds", "date_added": "2026-04-03"}` |
| pronunciation.csv exists | **CONFIRMED** | File exists (1,054 bytes) |
| morphology_reference.md exists | **CONFIRMED** | File exists (12,839 bytes) |
| morphology_context.md exists | **CONFIRMED** | File exists (22,742 bytes) |
| nt_grammar_stats.json exists | **CONFIRMED** | File exists (4,138 bytes) |

## Section 4: Data Formats

| Claim | Verdict | Evidence |
|-------|---------|----------|
| MorphGNT format: "Space-separated: BBCCVV POS morph-code text normalized lemma" (6 fields) | **CONTRADICTED** | Actual format has 7 space-separated fields: `010101 N- ----NSF- Βίβλος Βίβλος βίβλος βίβλος` (reference, POS, parsing, text, word, normalized, lemma) |
| Compounds enriched JSON: {lemma, components[], meaning_es, mnemonic_es, strongs_*, suffix*, root_note_es, cognates_by_part{}, greek_verses[]} | **PARTIALLY CONFIRMED** | Actual keys: ['lemma', 'components', 'meaning_es', 'mnemonic_es', 'first_ref', 'pos', 'strongs_number', 'strongs_derivation', 'strongs_definition', 'cognates', 'cognates_by_part', 'greek_verses']. Missing from claim: first_ref, pos, cognates (separate field). The "suffix*" and "root_note_es" fields exist in some entries |
| Compounds full JSON: {lemma, components[], meaning_es, root_note_es} | **CONFIRMED** | Actual keys: ['lemma', 'components', 'meaning_es', 'root_note_es'] |
| Lesson data format: {num, intro_es, dialogue, vocab[], phrases[], recon[], verse, closing_es} | **PARTIALLY CONFIRMED** | Actual keys include all of these PLUS `context_es` which is not mentioned in the findings |
| Terminaciones cards: Python lists of (front_html, back_html) tuples | **CONFIRMED** | Code uses `cards.append((front_string, back_string))` pattern |

## Section 5: TTS & Audio

| Claim | Verdict | Evidence |
|-------|---------|----------|
| Amazon Polly for Spanish (Mia, es-MX) | **CONFIRMED** | `def es(text, voice="Mia", engine="neural")` with `LanguageCode="es-MX"` |
| Google Cloud TTS for Greek | **CONFIRMED** | Uses `texttospeech.TextToSpeechClient()` with `language_code="el-GR"` |
| Chirp3-HD as primary Greek voice | **CONFIRMED** | `M = "el-GR-Chirp3-HD-Achird"`, `F = "el-GR-Chirp3-HD-Zephyr"` |
| "Chirp3-HD fails on short words (1-2 syllables) → fallback to Wavenet-B if audio < 400ms" | **CONTRADICTED** | The code does NOT use Wavenet-B. Fallback is to OTHER Chirp3-HD voices (Charon, Aoede, Zephyr, Kore, Achird). The lessons-learned doc mentions Wavenet-B but the actual code uses Chirp3-HD fallbacks. The 400ms threshold is also not exact — the code uses `_min_dur()` formula: `max(400, min(n,4)*150 + max(0,n-4)*80)` |
| `to_mono()` strips polytonic → monotonic before TTS | **CONFIRMED** | Function exists, strips diacritics keeping only OXIA/TONOS/ACUTE |
| TTS cached by content hash in /tmp/tts_cache/ | **CONFIRMED** | `CACHE = "/tmp/tts_cache"` with `_cache_path()` function |
| 90 lesson MP3s organized by level (3 levels × 30 lessons) | **CONFIRMED** | 3 directories (level1_el_extranjero, level2_el_discipulo, level3_el_predicador), 91 MP3s total in audio/ |
| serve_audio.py is HTTPS server | **CONFIRMED** | Uses `ssl.SSLContext`, loads cert.pem/key.pem |

## Section 6: LLM & Dependencies

| Claim | Verdict | Evidence |
|-------|---------|----------|
| Amazon Bedrock (Claude) for enrichment | **CONFIRMED** | `bedrock = boto3.client('bedrock-runtime')`, `MODEL = 'us.anthropic.claude-sonnet-4-20250514-v1:0'` |
| KOINE_ANKI_PATH env var for cross-repo dependency | **CONFIRMED** | `os.environ.get('KOINE_ANKI_PATH', ...)` in enrich.py, documented in README |
| koine-pimsleur depends on koine-anki/data/ for compounds_enriched.json and morphology_reference.md | **CONFIRMED** | enrich.py loads both files from ANKI_REPO path |
| Python 3.12 | **UNVERIFIED** | No version pinning found in any config file. System has Python 3.14. READMEs just say `python3` |
| Dependencies: genanki, py-sblgnt, google-cloud-texttospeech, boto3, pydub | **CONFIRMED** | All referenced in code imports and README setup instructions |
| Library name: "py-sblgnt" (pip) imported as `pysblgnt` | **CONFIRMED** | `pip install py-sblgnt` in README, `from pysblgnt import morphgnt_rows` in code |

## Section 7: Card Design Standards

| Claim | Verdict | Evidence |
|-------|---------|----------|
| Front: Greek word (36px, dark blue) + question prompt | **CONFIRMED** | card-quality-standards.md: "Word (36px, dark blue)" |
| Back sections: Word+meaning → 📦 Componentes → 🔤 Sufijo → 🔀 Cambio de raíz → 💡 Mnemotecnia → 🌍 Cognados → 📖 Versículos | **PARTIALLY CONFIRMED** | card-quality-standards.md lists only 5 sections (through Mnemotecnia). 🌍 Cognados and 📖 Versículos exist in generate_deck.py code but are NOT in the standards doc. The findings conflate the doc with the implementation |
| Cards must be 100% self-contained | **CONFIRMED** | Rule #1 in card-quality-standards.md |
| Every morpheme must be explained | **CONFIRMED** | Rule #2 in card-quality-standards.md |
| Mnemonics must tell a story | **CONFIRMED** | Rule #5 in card-quality-standards.md |
| Use simplified terminology (avoid formal grammar jargon) | **CONFIRMED** | Terminology table in koine-greek-anki-guidelines.md |

## Section 8: Koine vs Modern Greek Rules

| Claim | Verdict | Evidence |
|-------|---------|----------|
| Vocabulary blacklist: νερό→ὕδωρ, σπίτι→οἶκος, ψωμί→ἄρτος, πόρτα→θύρα | **CONFIRMED** | Exact match in lessons-learned-koine.md |
| False friends: παρακαλέω="beseech" not "please", δουλεύω="be a slave" not "work" | **CONFIRMED** | Exact match in lessons-learned-koine.md |
| Grammar Koine has that Modern lost: dative, infinitive, synthetic future, genitive absolute, declined participles | **CONFIRMED** | Exact match in lessons-learned-koine.md |
| Verification: Check against MorphGNT + LXX lemma lists | **CONFIRMED** | Documented in lessons-learned-koine.md |

## Section 9: NFC Normalization Claim

| Claim | Verdict | Evidence |
|-------|---------|----------|
| "Greek text MUST use NFC normalization" as a critical rule | **PARTIALLY CONFIRMED** | NFC normalization IS used in code (fetch_strongs.py, tts.py) but is NOT stated as a rule in any guidelines/standards doc. It's an implementation detail, not a documented "critical rule" |

## Section 10: Pimsleur Method Structure

| Claim | Verdict | Evidence |
|-------|---------|----------|
| 8-part lesson structure (opening dialogue through biblical verse + closing) | **CONFIRMED** | Exact match in lessons-learned-koine.md section 3 |
| 90 total lessons | **CONFIRMED** | 90 MP3s in decks/lessons_v2/, 19 lesson data files covering lessons 1-90 |

## Section 11: Pipeline Commands

| Claim | Verdict | Evidence |
|-------|---------|----------|
| `cd koine-anki && python compounds/generate_deck.py` | **CONFIRMED** | Matches README |
| `cd koine-anki && python terminaciones/gen_deck.py` | **CONFIRMED** | Matches README |
| `cd koine-anki && python terminaciones/gen_deck_vol3.py` | **CONFIRMED** | Matches README |
| `cd koine-pimsleur && python -m src.generate --lesson 5` | **CONFIRMED** | Matches README |
| `cd koine-pimsleur && python src/generate_decks.py` | **CONFIRMED** | Matches README |
| `cd koine-pimsleur && python src/enrich.py kiro-test/lesson_01_script.json` | **CONFIRMED** | Matches README |

---

## Summary

| Verdict | Count |
|---------|-------|
| CONFIRMED | 47 |
| PARTIALLY CONFIRMED | 5 |
| CONTRADICTED | 3 |
| UNVERIFIED | 1 |

### Key Contradictions:
1. **MorphGNT format**: Claims 6 fields, actual has 7 (missing the "word" field between text and normalized)
2. **Wavenet-B fallback**: The lessons-learned doc mentions this but the actual code uses other Chirp3-HD voices as fallbacks, NOT Wavenet-B. The code was likely updated after the doc was written.
3. **Strong's word count**: Claim says 5,516 but XML has 5,624 entries

### Key Partial Confirmations:
1. **Compounds enriched JSON schema**: Missing fields first_ref, pos, cognates from the claim
2. **Lesson data keys**: Missing context_es from the claim
3. **Card back sections**: 🌍 Cognados and 📖 Versículos exist in code but NOT in the standards doc
4. **NFC normalization**: Used in code but not documented as a "critical rule" anywhere
5. **es_rvr.json size**: 3.8MiB vs claimed 4MB (acceptable rounding)
