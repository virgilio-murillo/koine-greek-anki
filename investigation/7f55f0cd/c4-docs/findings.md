# C4-Docs Findings: AWS Documentation Investigation for anki-agent Enhancement

## Summary

AWS documentation has **no direct content** about Anki flashcards, deck generation, spaced repetition systems, or Koine Greek language tools. However, AWS docs provide highly relevant **prompt engineering best practices** that directly apply to enhancing the anki-agent prompt.

---

## Q1-Q4: Project-Specific Questions (Not in AWS Docs)

AWS documentation does not cover:
- Anki deck formats (.apkg, TSV, CSV for import)
- Spaced repetition algorithms
- Koine Greek text processing
- Bible study tools or lexicon data
- The `genanki` Python library or similar tools

**These questions must be answered by other investigation agents examining the local project.**

---

## Q5: What Should the Enhanced Prompt Contain?

Based on AWS Bedrock and Amazon Nova prompt engineering documentation, the following patterns are directly applicable:

### Recommended Prompt Structure (from AWS Nova System Role docs)

Source: https://docs.aws.amazon.com/nova/latest/userguide/prompting-system-role.html

AWS recommends a system prompt template with these sections:

```
1. persona       — "You are {{Persona}}"
2. model_instructions — "## Model Instructions\n{{ Bulleted list }}"
3. response_schema    — "## Response Schema\n{{ Output format }}"
4. guardrails         — "## Guardrails\n{{ DO NOT rules }}"
```

### Key Principles from AWS Docs

#### From Amazon Nova Prompting Best Practices
Source: https://docs.aws.amazon.com/nova/latest/userguide/prompting.html

Define the use case on **4 dimensions**:
1. **Task** — What the model should accomplish
2. **Role** — What persona/identity to assume
3. **Response Style** — Output structure/format for the consumer
4. **Instructions** — Step-by-step rules to follow

#### From General Prompting Tips
Source: https://docs.aws.amazon.com/nova/latest/userguide/prompting-general-tips.html

- **Task decomposition**: Break complex tasks into discrete steps
- **Instruction breakdown**: Use atomic, clear instructions
- **Avoid assumptions**: Provide direct, unambiguous guidance
- **Escaped Unicode warning**: Models can loop on escaped Unicode — instruct to use native characters (CRITICAL for Greek text: "Do NOT use escaped Unicode - use native characters")
- **Structure with markdown/bullets**: For information-dense prompts, use clear formatting

#### From Bedrock Advanced Prompt Templates
Source: https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts-templates.html

- Use `<guidelines>` XML tags to wrap critical rules
- Include thinking/reasoning steps before actions
- Use `<example>` tags for few-shot demonstrations
- System instructions supersede user instructions

#### From Prompt Engineering Concepts
Source: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-engineering-guidelines.html

- **Few-shot prompting**: Provide labeled input/output examples to calibrate behavior
- **Prompt template pattern**: instruction + context + input + examples
- **RAG for reducing hallucinations**: Ground responses in provided data

#### From Structured Output Guidance
Source: https://docs.aws.amazon.com/nova/latest/userguide/prompting-structured-output.html

- Define explicit **Output Schema** for consistent format
- Use `temperature=0` for deterministic structured output
- Prefill assistant response to enforce format

---

## Recommended Enhanced Prompt Architecture for anki-agent

Based on AWS documentation patterns, the enhanced ~1159 char prompt should be expanded to include:

### 1. Persona Section
```
You are an Anki deck generation specialist for Koine Greek biblical vocabulary.
```

### 2. Critical Rules / Guardrails (highest ROI per shared learnings)
```
## Critical Rules
- ALL Greek text MUST use NFC Unicode normalization
- DO NOT use escaped Unicode sequences — use native Greek characters
- Verify all lexical data against source files before output
- Output format must be valid TSV/CSV importable by Anki
```

### 3. Model Instructions (atomic steps)
```
## Instructions
1. Read source vocabulary data from the specified path
2. Validate Greek text encoding (NFC normalization)
3. Generate cards with: front (Greek), back (English gloss + parsing)
4. Apply deck-specific formatting rules
5. Output in the required import format
```

### 4. Response Schema
```
## Response Schema
Output as tab-separated values:
greek_word\tgloss\tparsing\ttags
```

### 5. Few-Shot Examples (per AWS recommendation)
```
<example>
Input: Generate a card for λόγος
Output: λόγος\tword, message\tnoun, masc, nom, sg\tkoine::nouns
</example>
```

---

## Limitations of This Investigation

1. **AWS docs are not authoritative** for Anki-specific formats, genanki library usage, or Koine Greek linguistic data
2. The prompt engineering patterns are **general best practices** — the specific content (vocabulary lists, parsing rules, deck structure) must come from examining the actual project files
3. No AWS documentation exists about the `bible-tools` project or `koine-anki/data/` referenced in the investigation questions

---

## Confidence Assessment

| Finding | Confidence | Source |
|---------|-----------|--------|
| Prompt structure pattern (persona + instructions + schema + guardrails) | HIGH | AWS Nova docs, confirmed pattern |
| Few-shot examples improve accuracy | HIGH | AWS Bedrock prompt engineering docs |
| Unicode/escaped chars cause model loops | HIGH | AWS Nova general tips |
| Critical Rules section = highest ROI | CONFIRMED | Shared learnings (seen: 7) |
| NFC normalization requirement | CONFIRMED | Shared learnings (seen: 3) |
| Specific Anki format details | NOT FOUND in AWS docs | Must come from project inspection |
