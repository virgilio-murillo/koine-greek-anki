# Koine Greek Anki Deck — Guidelines & Learnings

## User Profile
- Learning Koine Greek as a beginner
- Native Spanish speaker, also speaks English
- Card fronts should be in **Spanish**
- Does NOT know formal grammar terminology — avoid jargon or explain it simply

## Card Design Principles

### Front (Question)
- Written in Spanish
- Includes context about what grammatical concept is being tested
- Example: "¿A quiénes ayudas en tu comunidad? (plural pregunta por indirecto; pronombre interrogativo en masculino/femenino, plural, dativo)"

### Back (Answer) — MUST include:
1. **Answer word** in large text
2. **Full Greek phrase** highlighted in green
3. **Biblical reference** if applicable (italic, gray)
4. **Word-by-word breakdown** of EVERY word in the phrase, each in its own box with:
   - 📋 Grammatical parsing (case, gender, number, person)
   - 🔤 Root + ending breakdown
   - 💬 Spanish meaning in quotes
   - ❓ **Contrastive explanation** — WHY this ending and not others, showing what the word would look like in other cases/forms

### Contrastive Explanations (❓) — Critical Rules
- ALWAYS show what the alternatives would be: "Termina en X porque significa Y. Si fuera Z significaría W."
- For nouns/articles/pronouns: show all 4 case forms and what each means
  - Example: "Termina en -ου porque indica 'de...' (posesión). Si fuera -ος sería sujeto, si fuera -ῳ sería 'a/para...', si fuera -ον sería objeto directo."
- For verbs: show person contrasts
  - Example: "Termina en -εις porque es 'TÚ haces'. Compara: -ω (yo) → -εις (tú) → -ει (él/ella)."
- For participles: explain why it's NOT a regular adjective/noun
- For irregular forms (εἰμί, δίδωμι): say "irregular — memorize it"

## Terminology — Simplified Vocabulary
Use these simplified terms instead of formal grammar jargon:

| ❌ Don't use | ✅ Use instead |
|---|---|
| 1ª declinación | grupo -η/-α (fem.) |
| 2ª declinación | grupo -ος/-ον |
| 3ª declinación | grupo consonante |
| verbo contracto | verbo con fusión vocálica |
| forma enclítica | forma sin acento propio (se apoya en la palabra anterior) |
| verbo deponente | verbo con forma pasiva pero significado activo |
| iota suscrita | iota escondida debajo (ῳ, ῃ) |

## Deck Structure
- **Deck name**: "Koiné Griego – Pronombres (Mejorado)"
- **10 intro cards** (🔑 prefix) teaching foundational concepts: cases, word groups, contract verbs, how to read endings
- **57 grammar cards** with full word-by-word breakdowns
- **Model**: "Greek Pronouns Enhanced" (ID: 1646410861241) for grammar cards, "Greek Intro Concepts" (ID: 1646410861242) for intro cards

## Technical Setup
- Working directory: `~/work/anki/`
- Test/build environment: `~/work/anki/kiro-test/` (Python venv with playwright, genanki)
- Original deck: `~/work/anki/koine test 1.apkg` (57 cards, model "Basic+", fields: Front/Back/Notes)
- Enhanced deck output: `~/work/anki/koine_mejorado.apkg`
- Source code: `~/work/anki/kiro-test/generate_deck.py` (main generator)
- Lexicon files: `lexicon_part1.py` through `lexicon_part4.py` (155 Greek word entries)
- Contrast engine: `contrast_engine.py` (generates contrastive WHY explanations dynamically)
- Intro cards: `intro_cards.py` (10 foundational concept cards)

## APKG Format Notes
- .apkg files are zip archives containing `collection.anki2` (SQLite) and `media`
- Fields separated by `\x1f` (unit separator)
- Use `genanki` Python library to create new decks
- Card backs use HTML with inline CSS for styling (Anki renders HTML)
- Avoid `&nbsp;` — use CSS `padding-left` for indentation instead

## Greek Grammar Quick Reference (for generating new cards)

### Case Endings Cheat Sheet
| Case | Group -ος (masc.) | Group -η (fem.) | Group -ον (neut.) |
|---|---|---|---|
| Nom. sing. | -ος | -η / -α | -ον |
| Gen. sing. | -ου | -ης / -ας | -ου |
| Dat. sing. | -ῳ | -ῃ / -ᾳ | -ῳ |
| Acc. sing. | -ον | -ην / -αν | -ον |
| Nom. pl. | -οι | -αι | -α |
| Gen. pl. | -ων | -ων | -ων |
| Dat. pl. | -οις | -αις | -οις |
| Acc. pl. | -ους | -ας | -α |

### Universal Rules
- Genitive plural = **-ων** (always, all groups)
- Neuter plural = **-α** (always)
- Neuter: nominative = accusative (always identical)
- Iota (visible or subscript) = dative
- -ν at end of singular = accusative

### Verb Person Endings (Present Active)
| Person | Singular | Plural |
|---|---|---|
| 1st (yo/nosotros) | -ω | -ομεν |
| 2nd (tú/ustedes) | -εις | -ετε |
| 3rd (él/ellos) | -ει | -ουσι(ν) |

### Vowel Fusion Rules (contract verbs in -έω)
- ε + ω → ῶ
- ε + ει → εῖ  
- ε + ο → ου
- ε + ου → οῦ
