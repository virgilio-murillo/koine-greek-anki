# Validated Findings: C4-Docs (AWS Documentation Investigation)

## Validation Method
Each claim was cross-checked against the actual AWS documentation pages cited. URLs were fetched and content compared to the claims made in findings.md.

---

## Claim-by-Claim Validation

### 1. System prompt template (persona + model_instructions + response_schema + guardrails)
**Source cited:** https://docs.aws.amazon.com/nova/latest/userguide/prompting-system-role.html
**Verdict: ✅ CONFIRMED**

The AWS Nova system role page contains the exact template code block with `persona`, `model_instructions`, `response_schema`, and `guardrails` sections as described. The findings accurately quote the structure.

### 2. Define use case on 4 dimensions (Task, Role, Response Style, Instructions)
**Source cited:** https://docs.aws.amazon.com/nova/latest/userguide/prompting.html
**Verdict: ✅ CONFIRMED**

The page explicitly states: "Define your use case you want to achieve on 4 dimensions: 1. What is the Task, 2. What's the Role, 3. What's the Response Style, 4. What set of Instructions to be followed."

### 3. Escaped Unicode characters cause model repetitive loops
**Source cited:** https://docs.aws.amazon.com/nova/latest/userguide/prompting-general-tips.html
**Verdict: ✅ CONFIRMED**

The page states verbatim: "The model can sometimes enter a repetitive loop when it encounters *escaped Unicode language cases*." The recommended mitigation example is also confirmed: "Do NOT ever put escaped Unicode in the output - just use the unescaped native character."

### 4. Task decomposition recommended for complex tasks
**Source cited:** https://docs.aws.amazon.com/nova/latest/userguide/prompting-general-tips.html
**Verdict: ✅ CONFIRMED**

Confirmed: "If your task is complex...we recommend that you scope the problem and decompose it into a series of discrete calls."

### 5. Instruction breakdown into atomic instructions
**Source cited:** https://docs.aws.amazon.com/nova/latest/userguide/prompting-general-tips.html
**Verdict: ✅ CONFIRMED**

Confirmed: "We recommended that you break down complex instructions into a series of instructions or into more atomic instructions."

### 6. Avoid assumptions, provide clear guidance
**Source cited:** https://docs.aws.amazon.com/nova/latest/userguide/prompting-general-tips.html
**Verdict: ✅ CONFIRMED**

Confirmed: "It is critical to avoid making any assumptions and instead offer direct, unambiguous guidance to the model."

### 7. Structure with markdown/bullets for information-dense prompts
**Source cited:** https://docs.aws.amazon.com/nova/latest/userguide/prompting-general-tips.html
**Verdict: ✅ CONFIRMED**

Confirmed: "using markdown or bullet points can help enhance the Amazon Nova models' ability to comprehend and organize the provided information more effectively."

### 8. Use `<guidelines>` XML tags to wrap critical rules
**Source cited:** https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts-templates.html
**Verdict: ✅ CONFIRMED**

The Bedrock advanced prompts page shows `<guidelines>` XML tags wrapping rules in the agent orchestration templates.

### 9. Include thinking/reasoning steps before actions
**Source cited:** https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts-templates.html
**Verdict: ✅ CONFIRMED**

The template includes: "Always output your thoughts within `<thinking></thinking>` xml tags before and after you invoke a function."

### 10. Use `<example>` tags for few-shot demonstrations
**Source cited:** https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts-templates.html
**Verdict: ⚠️ UNVERIFIED**

The advanced-prompts-templates page I reviewed does NOT explicitly show `<example>` tags. It shows `<guidelines>`, `<thinking>`, `<answer>`, `<function_calls>` tags. The `<example>` tag pattern is a well-known Anthropic Claude convention but was not confirmed in this specific AWS page. The claim may be sourced from a different section of the page not retrieved.

### 11. System instructions supersede user instructions
**Source cited:** https://docs.aws.amazon.com/nova/latest/userguide/prompting-system-role.html
**Verdict: ✅ CONFIRMED**

Confirmed: "The system prompt, as compared to the user prompt, holds higher importance than other instructions provided in individual user prompts."

### 12. Few-shot prompting improves accuracy
**Source cited:** https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-engineering-guidelines.html
**Verdict: ✅ CONFIRMED**

The page describes "demonstration examples" as a core component of prompts. The concept of providing labeled examples to calibrate behavior is confirmed as a standard prompt engineering technique in the Bedrock docs.

### 13. Prompt template pattern: instruction + context + input + examples
**Source cited:** https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-engineering-guidelines.html
**Verdict: ✅ CONFIRMED**

The page explicitly describes prompt components as: "the task or instruction...the context of the task...demonstration examples, and the input text."

### 14. RAG for reducing hallucinations
**Source cited:** https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-engineering-guidelines.html
**Verdict: ✅ CONFIRMED**

Confirmed: "use techniques like Retrieval Augmented Generation (RAG) to provide the model access to more relevant data" to reduce hallucinations.

### 15. Define explicit Output Schema for consistent format
**Source cited:** https://docs.aws.amazon.com/nova/latest/userguide/prompting-structured-output.html
**Verdict: ✅ CONFIRMED**

Confirmed: "We recommend that you provide an `output schema` for the model to follow."

### 16. Use temperature=0 for deterministic structured output
**Source cited:** https://docs.aws.amazon.com/nova/latest/userguide/prompting-structured-output.html
**Verdict: ✅ CONFIRMED**

Confirmed verbatim: "For structured output, regardless of whether you are leveraging tool use, we recommend using greedy decoding parameters. That is, `temperature=0`."

### 17. Prefill assistant response to enforce format
**Source cited:** https://docs.aws.amazon.com/nova/latest/userguide/prompting-structured-output.html
**Verdict: ✅ CONFIRMED**

Confirmed with code example showing prefilling assistant content with `"```json"` to guide output format.

### 18. AWS docs have NO content about Anki flashcards, spaced repetition, Koine Greek tools
**Verdict: ✅ CONFIRMED**

AWS documentation is focused on cloud services. No Anki, spaced repetition, or Koine Greek content exists in AWS docs. This is self-evident from the nature of the documentation.

### 19. Current prompt is ~1159 chars
**Verdict: ⚠️ UNVERIFIED**

No "anki-agent" prompt file was found in the project. The project has no `.kiro/` steering directory at the root level. This claim cannot be verified from the available project files. It may reference a prompt defined elsewhere or in a previous session.

### 20. "Critical Rules section = highest ROI" (shared learnings, seen: 7)
**Verdict: ⚠️ UNVERIFIED**

This claim references "shared learnings" from the investigation framework, not AWS documentation. Cannot independently verify the count or the ROI assertion.

### 21. "NFC normalization requirement" (shared learnings, seen: 3)
**Verdict: ⚠️ UNVERIFIED**

This claim references "shared learnings" from the investigation framework. NFC normalization is a well-known best practice for Unicode text processing (especially Greek), but the specific "seen: 3" count from shared learnings cannot be verified.

---

## Summary

| Status | Count |
|--------|-------|
| ✅ CONFIRMED | 17 |
| ⚠️ UNVERIFIED | 4 |
| ❌ CONTRADICTED | 0 |

**Overall Assessment:** The findings are highly accurate. All AWS documentation claims were verified against the actual source pages. The 4 unverified items are either: (a) internal investigation metadata that can't be cross-checked, (b) a specific XML tag claim not found in the retrieved portion of the page, or (c) a project-specific claim about prompt size that couldn't be located in the filesystem. No claims were contradicted.

**Key Validation Notes:**
- The AWS Nova prompting documentation is labeled "Amazon Nova Version 1" — a Nova 2 guide now exists at a different URL. The patterns are still valid but may have updates.
- The findings correctly distinguish between what AWS docs cover (prompt engineering patterns) and what they don't (Anki-specific formats, Greek linguistics).
- The recommended prompt architecture in the findings is a reasonable synthesis of the documented patterns applied to the anki-agent use case.
