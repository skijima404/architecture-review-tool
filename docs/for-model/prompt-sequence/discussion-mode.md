# Discussion Mode Prompt Template

## Purpose
The Discussion Mode phase is designed for interactive exploration, clarification, and ideation around architecture review findings. The goal is to collaboratively deepen understanding, challenge assumptions, and resolve ambiguities before moving on to formal action extraction.

## When to Use
Discussion Mode should be initiated after summary generation (e.g., after AAR candidate findings are produced) and before action extraction (AAR creation). It serves as an intermediate step to refine findings and context.

## Inputs
- **Summarized Findings:** Architecture Assessment Report (AAR) candidate findings or summary output from prior steps.
- **GraphDB Dependency Data:** Relevant dependency graphs or extracted system relationships.
- **Clarifying Context:** Any additional context, questions, or uncertainties identified during earlier review phases.

## Outputs
- **Refined Understanding:** Improved clarity and shared understanding of each finding.
- **Prioritized Discussion Points:** A list of key findings or issues prioritized for further action.
- **Clarified Context:** Documented clarifications, resolved ambiguities, and rationale for each discussed point.

## Prompt Example
```markdown
You are now entering Discussion Mode. The purpose of this phase is to collaboratively explore, clarify, and deepen understanding of the following architecture review findings before formal action extraction.

**Inputs:**
- Summarized findings (AAR candidates): [Paste findings here]
- GraphDB dependency data: [Paste or describe data here]
- Additional context: [Paste context/questions here]

**Instructions:**
- Engage in iterative discussion about the findings.
- Ask clarifying questions where information is ambiguous or incomplete.
- Challenge assumptions and encourage alternative perspectives.
- Identify and prioritize findings that require further analysis or action.
- Document clarifications, rationale, and any newly surfaced insights.

**Discussion Starter:**
For each finding, please:
1. Restate the finding in your own words.
2. Identify any unclear aspects or assumptions.
3. Pose clarifying questions or suggest alternative interpretations.
4. Propose next steps for refining the finding or resolving uncertainties.

Proceed through the findings one at a time, ensuring each is fully explored before moving on.
```