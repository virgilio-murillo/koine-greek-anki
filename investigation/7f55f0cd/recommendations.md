# Early Recommendations — anki-agent Enhancement
_Updated: 2026-05-24 by HEAD AGENT_

## Status: HIGH CONFIDENCE — All 4 child agents completed

---

## 1. Critical Bug Fix (Highest Priority)

**Current prompt says:**
> `koine-anki/data/ is referenced by bible-tools ingest_local.py`

**This is WRONG.** Verified by reading `koine-pimsleur/src/enrich.py` directly.

**Actual consumer:** `koine-pimsleur/src/enrich.py` reads `koine-anki/data/matthew/compounds_enriched.json` and `data/morphology_reference.md` via `KOINE_ANKI_PATH` env var (defaults to sibling placement).

**Fix:** Replace the incorrect sentence with:
> `koine-anki/data/ is consumed by koine-pimsleur/src/enrich.py via KOINE_ANKI_PATH env var`

---

## 2. TTS Fallback Correction

**Current notes say:** "if < 400ms, retry with Wavenet-B"

**Actual code behavior (verified in tts.py):**
- Short words: threshold is **character count < 4 Greek chars** (not duration)
- Fallback is **other Chirp3-HD voices** (FALLBACK_M/FALLBACK_F lists), NOT Wavenet-B
- Normal words: `_min_dur()` formula = `max(400, min(n,4)*150 + max(0,n-4)*80)` ms
- Failures logged to `/tmp/tts_cache/tts_qa_report.txt`

**Prompt should say:** "Short words (<4 Greek chars) try all Chirp3-HD voices in gender pool; normal words use min-duration formula with Chirp3-HD fallback pool"

---

## 3. Missing Architecture Details

The enhanced prompt must add:

### Compounds Pipeline (5 steps)
```
extract_compounds.py → fetch_strongs.py → enrich_compounds.py → [enrich_cognates.py + enrich_verses.py + add_rvr60.py] → generate_deck.py
```
- Input: MorphGNT via py-sblgnt
- Output: `data/matthew/compounds_enriched.json` → `decks/matthew_compounds.apkg`
- Anti-duplication: `data/compounds_registry.json` (290 entries, keyed by lemma)

### Terminaciones Formats
- Vol. 2 (`gen_deck.py`): outputs **TSV** (`greek_infinitives_anki.txt`) — Anki text import
- Vol. 3 (`gen_deck_vol3.py`): outputs **.apkg** via genanki

### Pimsleur Deck Selection
- 4 cards/lesson: 2 vocab + 1 phrase + 1 verse (fills from remaining vocab if needed)
- Recognition (Greek→Spanish) + Production (Spanish→Greek) templates

---

## 4. Missing Critical Rules

Add to Critical Rules section:

1. **NFC normalization**: All Greek text stored as NFC. `fetch_strongs.py` normalizes on ingest. `tts.py` uses NFD internally for `to_mono()` then re-normalizes to NFC.
2. **Stable deck IDs**: Pimsleur model=1646410900000, Compounds model=1646410861305, Terminaciones Vol.3 model=1607392319. Never change these.
3. **compounds_registry.json**: Before processing a new NT book, dedup against this registry. 290 Matthew entries already registered.
4. **Vocabulary blacklist** (Modern Greek contamination): νερό→ὕδωρ, σπίτι→οἶκος/οἰκία, ψωμί→ἄρτος, πόρτα→θύρα. All Turkish/Italian loanwords (post-1453) are banned.
5. **TTS fallback**: Short words (<4 Greek chars) → try all Chirp3-HD voices in gender pool. NOT Wavenet-B.
6. **Spanish-first**: Card fronts in Spanish. Explanations in Spanish. Simplified terminology (no formal grammar jargon).
7. **KOINE_ANKI_PATH**: Set this env var when running koine-pimsleur scripts outside sibling placement.

---

## 5. Active Subproject Status

| Subproject | Status | Active Scripts |
|---|---|---|
| `koine-anki/compounds/` | ✅ Active | 10 scripts (4 new: enrich_cognates, audit_cognates, enrich_verses, add_rvr60) |
| `koine-anki/terminaciones/` | ✅ Active | gen_deck.py (TSV), gen_deck_vol3.py (.apkg) |
| `koine-pimsleur/src/` | ✅ Active | 9 scripts + 23 lesson data files |
| `anki-main/languages/src/` | ❌ Frozen | Monorepo from Apr 6 — do NOT edit |

---

## 6. Build & Run Commands

```bash
# koine-anki: Compounds deck
cd ~/work/github/anki/koine-anki
python compounds/generate_deck.py          # → decks/matthew_compounds.apkg

# koine-anki: Terminaciones
python terminaciones/gen_deck.py           # → terminaciones/greek_infinitives_anki.txt (TSV)
python terminaciones/gen_deck_vol3.py      # → terminaciones/terminaciones_vol3.apkg

# koine-pimsleur: Generate audio lesson
cd ~/work/github/anki/koine-pimsleur
source venv/bin/activate
python -m src.generate --lesson 5          # single lesson
python -m src.generate --range 1 10        # range
python -m src.generate --all               # all 90

# koine-pimsleur: Enrich lesson script
python src/enrich.py kiro-test/lesson_01_script.json

# koine-pimsleur: Generate Anki decks from lessons
python src/generate_decks.py               # → decks/anki/*.apkg
```

---

## 7. Bedrock Model

`enrich.py` uses: `us.anthropic.claude-sonnet-4-20250514-v1:0` (us-east-1, max_tokens=12000)
