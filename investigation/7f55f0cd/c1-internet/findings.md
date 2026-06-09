# Internet Research Findings: Enhance anki-agent

## 1. Deck Generation Tools (Ecosystem)

### Primary Tool: genanki (Python)
- **Repo**: https://github.com/kerrickstaley/genanki
- **PyPI**: https://pypi.org/project/genanki/0.13.1/
- **Purpose**: Programmatically generate .apkg decks in Python 3
- **Key API**:
  - `genanki.Model(model_id, name, fields=[], templates=[], css='')` — defines card types
  - `genanki.Note(model=, fields=[])` — a fact to memorize
  - `genanki.Deck(deck_id, name)` — container for notes
  - `genanki.Package(deck).write_to_file('output.apkg')` — exports
  - `package.media_files = ['file.mp3', 'image.jpg']` — attach media
- **Critical details**:
  - Model IDs and Deck IDs must be unique, hardcoded integers (use `random.randrange(1 << 30, 1 << 31)`)
  - Note GUIDs default to hash of all fields; override for stable updates
  - Fields are HTML — must use `html.escape()` for literal `<`, `>`, `&`
  - Media referenced in fields as `[sound:filename.mp3]` or `<img src="filename.jpg">`
  - Only basename (no path) in field references

### Alternative Tools
- **anki-apkg-export** (JS): https://github.com/repeat-space/anki-apkg-export — Node.js alternative
- **genanki-js**: https://github.com/krmanik/genanki-js — browser-side generation
- **pyanki**: https://github.com/maxwellpirtle/pyanki — Anki-Connect API wrapper
- **mkanki**: https://github.com/nornagon/mkanki — supports cloze + media

### Automation Patterns
- **Enderzombie/automated-apkg-creation**: JSON → apkg pipeline
- **DahnJ/Anki-Deck-Generation**: Python + genanki automated workflow
- **ThisIsntTheWay/anki-deck-automation**: Full build/export automation

## 2. File Formats

### .apkg (Primary Output)
- ZIP archive containing:
  - `collection.anki2` — SQLite database with notes, cards, models, decks
  - `media` file — JSON mapping of numeric filenames to original names
  - Numbered media files (0, 1, 2...) — the actual audio/image files
- Source: https://docs.ankiweb.net/exporting.html

### Import Formats (Input)
- **CSV/TSV**: Tab or semicolon-separated fields, importable directly into Anki
  - First line can specify separator: `separator:Tab` or `separator:Comma`
  - Tags column supported
  - Source: http://docs.ankiweb.net/importing/text-files.html
- **JSON**: Common intermediate format for data pipelines (used by automated-apkg-creation)

### Data Source Formats (for Greek vocab)
- **JSON**: bible-tools/data stores translations as JSON
- **TSV/CSV**: STEPBible-Data uses TSV with morphology codes
- **XML**: Perseus Digital Library canonical Greek texts

## 3. Koine Greek Data Sources & bible-tools Relationship

### bible-tools/data
- **URL**: https://github.com/bible-tools/data
- **Content**: Bible translations stored as JSON
- **Likely relationship**: `koine-anki/data/` probably references or symlinks to this repo for source vocabulary data

### STEPBible-Data
- **URL**: https://github.com/STEPBible/STEPBible-Data
- **License**: CC BY 4.0
- **Content**: TEGMC (Translators Expansion of Greek Morphology Codes), tagged Greek text with lemmas, parsing, glosses

### greek-learner-texts/vocabulary-data
- **URL**: https://github.com/greek-learner-texts/vocabulary-data
- **Content**: Consolidated vocabulary data for Greek learner texts project
- **Relevance**: Frequency lists, lemmatization, glosses for Koine Greek

### Existing Koine Greek Anki Decks (ankiweb.net)
- "All Bible Greek Vocab 2021" — all NT words, 4 subdecks by frequency (95% coverage at 6+ occurrences)
- "NT Greek Vocab (Oak Hill College)" — 1000 most common NT words
- "Living Koine Greek deck" — phonemic approach
- Multiple frequency-sorted decks exist

## 4. Pimsleur + Anki Pattern

Based on search results, the `koine-pimsleur/` directory likely:
- Generates Anki cards from Pimsleur-style audio lesson vocabulary
- Includes audio files (mp3) for pronunciation
- Uses phrase-based cards (not just single words)
- Follows the Pimsleur graduated-interval recall method adapted to Anki's SRS

Examples found: mipmc/anki (Pimsleur Mandarin), multiple Pimsleur companion decks on ankiweb.net with audio.

## 5. Unicode/Greek Text Critical Rules

### NFC Normalization (CONFIRMED CRITICAL)
- **Source**: https://www.katabiblon.com/tech/unicode-nf-greek.htm
- Greek text MUST use NFC normalization for consistent comparison and display
- NFKC normalizes characters outside U+0386–U+03CE (Greek/Coptic) and U+1F00–U+1FFF (Greek Extended) into those ranges
- NFC composes combining characters (e.g., base + diacritic → precomposed form)
- **Python**: `unicodedata.normalize('NFC', text)` — MUST be applied to all Greek text before storage/comparison
- **Source**: https://www.pgdp.net/wiki/DP_Code_-_Unicode/Greek confirms NFC is critical for Greek processing

### HTML Escaping
- genanki fields are HTML — Greek text with special chars needs `html.escape()`
- But Greek diacritics (breathing marks, accents) are Unicode, not HTML entities

## 6. Enhanced Prompt Recommendations

### Structure (Based on Best Practices Research)

The agent prompt should follow a **4-section structure** (per roborhythms.com research on agent tool hallucination prevention):

1. **Role & Scope** — What the agent does, domain context
2. **Tools & Schemas** — Available tools, data formats, file paths
3. **Critical Rules** (highest ROI per shared learnings) — Non-negotiable constraints
4. **Output Format** — Expected outputs, file naming, validation

### Recommended Critical Rules for anki-agent:
1. **NFC Normalization**: ALL Greek text MUST be `unicodedata.normalize('NFC', text)` before any processing
2. **Stable GUIDs**: Override Note.guid to hash only identity fields (not all fields) for safe re-imports
3. **HTML Escaping**: Use `html.escape()` for field content, but preserve Unicode Greek characters
4. **Hardcoded IDs**: Model and Deck IDs must be stable integers (never regenerate)
5. **Media Basenames**: Only use filename (no path) in `[sound:x]` or `<img src="x">` references
6. **Verify Against Source**: Cross-check generated vocab against authoritative data (STEPBible, bible-tools)
7. **Atomic Cards**: Follow Andy Matuschak's principles — one fact per card, encode from multiple angles

### Andy Matuschak's SRS Prompt Principles (Source: andymatuschak.org/prompts/)
- Prompts should focus on one atomic unit
- Encode ideas from multiple angles (not just one cloze)
- Make clear what "shape" of answer is expected
- Avoid yes/no prompts
- Discourage shallow pattern matching
- Connect and relate ideas
- Write more prompts than seems natural
- Properties: focused, precise, consistent, tractable, effortful, context-independent

## 7. Summary of What Enhanced Prompt Should Contain

Based on all research, the enhanced anki-agent prompt (~2000-3000 chars recommended) should include:

```
## Role
You are an Anki deck generation agent for Koine Greek biblical vocabulary...

## Project Structure
- anki-main/: [core shared utilities, genanki wrappers]
- koine-anki/: [NT vocabulary deck generation, data/ from bible-tools]
- koine-pimsleur/: [Pimsleur-style audio phrase cards]

## Critical Rules
1. Greek text: ALWAYS apply unicodedata.normalize('NFC', text)
2. genanki fields are HTML: use html.escape() but preserve Unicode
3. Model/Deck IDs: use existing hardcoded values, never regenerate
4. Note GUIDs: override to hash only identity fields for stable updates
5. Media: reference by basename only in fields
6. Verify vocab against source data before generating
7. One atomic fact per card; encode from multiple angles

## Tools & Formats
- genanki for .apkg generation
- Source data: JSON/TSV from bible-tools/data or STEPBible
- Output: .apkg files with embedded media
- CSV/TSV as intermediate format

## Output Expectations
- Generated decks must import cleanly into Anki
- All Greek text NFC-normalized
- Cards follow SRS best practices (atomic, precise, effortful)
```

---

## Sources
- genanki README: https://github.com/kerrickstaley/genanki
- Anki Manual (export/import): https://docs.ankiweb.net/exporting.html
- katabiblon Unicode Greek Normalization: https://www.katabiblon.com/tech/unicode-nf-greek.htm
- Andy Matuschak on prompts: https://andymatuschak.org/prompts/
- bible-tools/data: https://github.com/bible-tools/data
- STEPBible-Data: https://github.com/STEPBible/STEPBible-Data
- Agent prompt structure: https://www.roborhythms.com/fix-agent-tool-hallucinations-4-section-prompt/
- DP Code Unicode/Greek: https://www.pgdp.net/wiki/DP_Code_-_Unicode/Greek
