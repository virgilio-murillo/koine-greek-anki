# Compounds Pipeline — Full Reproduction Guide

## Overview
This pipeline creates Anki cards for compound Koine Greek words. Each card shows a compound word on the front, and on the back: its components, etymology, suffix explanation, root-change notes, and a mnemonic in Spanish.

## The Pipeline (5 steps)

### Step 1: Extract compound candidates
`src/extract_compounds.py` uses `py-sblgnt` (MorphGNT) to extract all unique lemmas from a book, then filters for compound candidates using a prefix list.

**Book numbers**: 1=Matthew, 2=Mark, 3=Luke, ..., 27=Revelation

**Prefix list used**: ἀπο, ἐπι, κατα, παρα, συν, ἀντι, ὑπο, ὑπερ, προσ, εἰσ, ἐκ, μετα, περι, δια, ἀνα, πρό, ἐν, εὐ, φιλ, ψευδ, πολυ, μισ, ὀλιγ, μονο, ὁμο, ἀ, δυσ

**Output**: `data/<book>/compounds_raw.json` — list of `{lemma, pos, first_ref}`

**For Matthew**: 349 candidates extracted, 59 filtered as false positives → 290 true compounds.

### Step 2: Decompose compounds (LLM STEP — NOT AUTOMATED)
This is the most labor-intensive step. An LLM must analyze each candidate and produce:
- `components`: [{greek, meaning_es}] — the parts that make up the word
- `meaning_es`: Spanish meaning
- `mnemonic_es`: mnemonic in Spanish

**Critical lessons learned:**
1. **Filter false positives**: Many words starting with ἀ- are NOT compounds (ἀγάπη, ἀγαθός, ἀκούω, etc.). Only ἀ-privative (ἀ- = "sin") and ἀ-copulative (ἀ- = "mismo") are real compounds.
2. **59 false positives were filtered from Matthew** — see `old/data/` for the full list.
3. Process in batches of ~50-100 words grouped by prefix.

**Output format** (JSON array):
```json
{
  "lemma": "ἐπιτρέπω",
  "components": [
    {"greek": "ἐπί", "meaning_es": "sobre"},
    {"greek": "τρέπω", "meaning_es": "voltear"}
  ],
  "meaning_es": "permitir",
  "mnemonic_es": "..."
}
```

### Step 3: Enrich with Strong's + suffixes + root notes
`src/fetch_strongs.py` — Adds Strong's etymology for the compound AND each component.
`src/enrich_compounds.py` — Adds suffix explanations and root-change notes.

**Key data built into enrich_compounds.py:**
- `SUFFIX_DB`: 11 Greek suffixes with Spanish explanations (-τός, -σις, -μα, -ία, -μός, -ή, -ικός, -ιος, -ών, -τής, -εια)
- `ROOT_CHANGES`: 45 words where the verb root changes form in derivatives (βάλλω→βολ-, τίθημι→θε-/θηκ-, ἵστημι→στα-, στέλλω→στολ-, ἵημι→ε-, etc.)

### Step 4: Improve mnemonics
`src/improve_mnemonics.py` — Replaces short/unhelpful mnemonics with full explanations.

**Quality criteria for mnemonics:**
- Must be >40 characters (short = useless)
- Must explain WHY the components lead to the meaning (not just "X + Y")
- Should include biblical reference when relevant
- Should include Spanish/English cognate when available
- For opaque etymologies (ἐπιτρέπω = "turn over" → permit), must explain the semantic chain

### Step 5: Generate Anki deck
`src/generate_deck.py` — Creates .apkg with styled HTML cards.

**Card structure:**
- Front: Greek word + "¿De qué se compone esta palabra?"
- Back: Word (large) → Meaning (green) → Ref + Strong's # → Components with Strong's definitions → Suffix box (purple) → Root-change box (orange) → Mnemonic box (green)

### Step 6: Update registry
After generating, update `data/compounds_registry.json` so future books don't duplicate cards.

## Anti-Duplication System
`data/compounds_registry.json` maps each processed lemma to its source book:
```json
{"ἀπολύω": {"source_book": "matthew", "deck": "matthew_compounds", "date_added": "2026-04-03"}}
```
When processing Mark, filter out any lemma already in the registry.

## Data Quality Issues Found (and fixed)

### Problem 1: Opaque etymologies
Some compounds have meanings that don't obviously follow from their parts:
- ἐπιτρέπω (ἐπί + τρέπω) = "turn over (transfer)" → permit
- διαστέλλομαι (διά + στέλλω) = "set apart clearly" → command strictly
- πρόβατον (πρό + βαίνω) = "walks forward (quadruped)" → sheep

**Solution**: Strong's definitions explain the semantic chain. Always include Strong's derivation.

### Problem 2: Missing suffix explanations
41 cards had suffixes (-σις, -μα, -ία, -τός, etc.) that weren't explained.

**Solution**: `SUFFIX_DB` in enrich_compounds.py auto-detects and explains suffixes.

### Problem 3: Invisible root changes
28 cards had verb roots that change form in derivatives (βάλλω→βολ-, τίθημι→θε-).

**Solution**: `ROOT_CHANGES` dict maps each affected word to its explanation.

### Problem 4: Short/useless mnemonics
191 cards had mnemonics like "quemar-completamente" — just literal translations, not helpful.

**Solution**: improve_mnemonics.py replaces them with full explanations including context, biblical refs, and cognates.

### Problem 5: False positive ἀ- words
~40 words starting with ἀ- were NOT compounds (ἀγάπη, ἀκούω, ἀστήρ, etc.).

**Solution**: Manual filtering. The false positive list is in old/data/.

## For the Septuagint (Future)
- LXX lemmas available at `openscriptures/GreekResources/LxxLemmas/` (60 books, JSON)
- Format: `{"Gen.1.1": [{"key": "ποιεω", "lemma": "ποιέω"}, ...], ...}`
- ~14,174 unique lemmas, ~3,077 compound candidates
- Same pipeline applies, but need to adapt extract_compounds.py to read LXX JSON instead of py-sblgnt
- Dedup against NT registry to avoid ~1,467 overlapping compounds
