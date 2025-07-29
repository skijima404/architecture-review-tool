# 📁 architecture-review-tool Directory Structure (as of 2025-06-04)

This repository provides a lightweight, GitHub-based toolkit to support architecture review activities. It includes reusable templates, decision records, review logs, and example cases. Below is the current directory structure with descriptions.

---

## 📦 Top-Level Structure

```plaintext
architecture-review-tool/
├── README.md                  # Project overview and usage
├── LICENSE
├── .gitignore
├── .github/
│   └── ISSUE_TEMPLATE.md      # (Optional) Issue or request template
├── docs/                      # Documentation
│   ├── for-humans/            # Guides and documentation for human readers
│   │   ├── README.md
│   │   └── user-guide.md
│   ├── for-model/             # Contextual data for AI (e.g., ChatGPT)
│	│   ├── review-model-design/
│	│   │   └── graph-ai-handoff-plan.md
│   │   ├── usage-guides/      # How to use this repository and its tools
│   │   │   └── directory-structure.md
│   │   ├── design-notes/      # Architecture review model structure and rationale
│   │   │   ├── architecture-review-axes.md
│   │   │   ├── review-layering.md
│   │   │   └── togaf-review-guide.md
│   │   ├── context.md
│   │   ├── llm-threshold-notes.md
│   │   ├── prompt-sequence/       # Execution order and prompt workflow for AI-assisted review
│   └── adr/                   # Architecture Decision Records for this tool itself
│       ├── 0001-record-format.md
│       └── 0002-github-structure.md
├── shared/                    # General templates for reuse
│   ├── adr-template.md
│   ├── review-log-template.md
│   ├── principles-template.md
│   └── prompts/
│       ├── 01_intro-template.md
│       ├── 02_roleplay-template.md
│       └── 03_reflection-template.md
├── samples/                   # Sample use cases (training or demos)
│   └── case-legacy-system/
│       ├── adr/
│       ├── principles/
│       ├── review-log/
│       └── prompts/
├── scripts/                   # Helper scripts (e.g., generation/build)
│   └── run-backcasting-extraction-byid.py
├── ai-memory/                 # Local dev notes and external memory for AsistA (ChatGPT)
├── templates/
│   ├── prompts/              # Reasoning prompt templates (e.g., backcasting, roll-up)
│   │   ├── backcasting/
│   │   └── rollup/
│   └── queries/              # Cypher query templates categorized by use case
│       ├── backcasting/
│       │   ├── from-sc.cypher
│       │   ├── root-cause.cypher
│       │   └── symptom.cypher
│       └── rollup/
│           ├── from-rc.cypher
│           ├── retrieve-edges.cypher
│           └── retrieve-nodes.cypher
├── runs/                     # Logs of prompt executions and LLM outputs
│   ├── 2025-07-08-sc-001-backcasting.md
│   └── 2025-07-08-rc-014-impact.md
```

⸻

🔍 Roles of GitHub in This Toolkit
	1.	External Memory for ChatGPT (AsistA)
→ Documents in docs/for-model/, docs/adr/, shared/ serve as context inputs
	2.	Architecture Repository (Review Targets)
→ samples/case-*/adr/, principles/, and prompts/ hold design data to be reviewed
	3.	Review Records (Outcomes)
→ samples/case-*/review-log/ stores review results in Markdown (based on templates)

- `prompt-sequence/`: Stores prompt execution flow and sequence-specific instructions for ChatGPT to follow.


├── templates/
│   ├── prompts/              # Reasoning prompt templates (e.g., backcasting, roll-up)