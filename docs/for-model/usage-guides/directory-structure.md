# 📁 architecture-review-tool Directory Structure (as of 2025-01-23)

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
│   │   ├── user-guide.md
│   │   ├── architecture-review-axes.md
│   │   └── togaf-review-guide.md
│   ├── for-model/             # Contextual data for AI (e.g., ChatGPT)
│   │   ├── context.md         # Project purpose and goals
│   │   ├── design-notes/      # Architecture review model structure and rationale
│   │   │   ├── adr-aar-policy.md
│   │   │   ├── architecture-advisory-record.md
│   │   │   ├── architecture-review-axes.md
│   │   │   ├── interaction-3mode-design.md
│   │   │   ├── llm-threshold-notes.md
│   │   │   ├── mvp2-rag-architecture.md
│   │   │   ├── review-layering.md
│   │   │   └── review-methodology.md
│   │   ├── prompt-sequence/   # 9-phase prompt workflow for AI-assisted review
│   │   │   ├── review-prompt-sequence.md  # Overview and flow diagram
│   │   │   ├── initialize.md              # Phase 1: Initialize
│   │   │   ├── install-templates.md       # Phase 2: Install Templates  
│   │   │   ├── collect-architecture-inputs.md  # Phase 3: Collect Inputs
│   │   │   ├── inject-graphdb-nodes.md    # Phase 4: Inject GraphDB
│   │   │   ├── clarification.md           # Phase 5: Clarification
│   │   │   ├── deep-collect.md            # Phase 5a: Deep Collect
│   │   │   ├── generate-draft-findings.md # Phase 6: Generate Draft Findings
│   │   │   ├── discussion-mode.md         # Phase 7: Discussion Mode
│   │   │   ├── extract-actions.md         # Phase 8: Action Extraction  
│   │   │   └── final-report-generation.md # Phase 9: Final Report Generation
│   │   ├── rag-architecture/  # RAG system design for automation
│   │   │   └── rag-architecture-diagram.mmd
│   │   ├── review-model-design/
│   │   │   └── graph-ai-handoff-plan.md
│   │   └── usage-guides/      # How to use this repository and its tools
│   │       └── directory-structure.md
│   ├── adr/                   # Architecture Decision Records for this tool itself
│   │   └── adr-0001-node-type-identitfication.md
│   └── reference-models/      # Reference materials and design artifacts
│       └── backcasting/
├── shared/                    # General templates for reuse
│   ├── adr-template.md
│   ├── review-log-template.md
│   ├── principles-template.md
│   └── prompts/
│       ├── 01_intro-template.md
│       ├── 02_roleplay-template.md
│       └── 03_reflection-template.md
├── samples/                   # Sample use cases (training or demos)
│   ├── input/                 # Input format samples and WIP examples
│   └── case-legacy-system/
│       ├── adr/
│       ├── principles/
│       ├── review-log/
│       └── prompts/
├── scripts/                   # Helper scripts (e.g., generation/build)
│   └── run-backcasting-extraction-byid.py
├── ai-memory/                 # Local dev notes and external memory for AsistA (ChatGPT)
├── templates/                 # Template files for architecture review process
│   ├── reports/              # Report templates by phase
│   │   ├── phase-6/          # Draft findings phase
│   │   │   └── draft-findings-table.md  # Draft findings with horror stories
│   │   └── phase-9/          # Final deliverables phase
│   │       ├── executive-summary.md     # Business leadership overview
│   │       ├── action-plan.md           # Implementation task breakdown
│   │       ├── traceability-record.md   # Success Criteria → Actions mapping
│   │       └── individual-aar.md        # Advisory record template (one per finding)
│   ├── prompts/              # AI prompt templates for GraphDB reasoning
│   │   ├── initialize.md     # Role and context setting
│   │   └── sc-review-backcast.yaml
│   ├── queries/              # Cypher query templates for GraphDB analysis
│   │   ├── backcasting/      # Success Criteria → Root Cause traversal
│   │   │   ├── from-sc.cypher
│   │   │   ├── root-cause.cypher
│   │   │   ├── success-criteria.cypher
│   │   │   └── symptom.cypher
│   │   └── rollup/           # Bottom-up analysis queries
│   └── legacy/               # Deprecated templates (for reference)
│       ├── aar-sample.md
│       ├── adr-sample-idp-selection.md
│       ├── prioritized-findings-table.md
│       └── report-output-summary.md
├── review-log/                # Session-based review records (input + output)
│   ├── review-001/
│   │   ├── input/              # Materials before review (SC, RC, context, artifacts)
│   │   └── output/             # Results after review (AAR, ADR drafts, summaries, transcripts)
│   ├── review-002/
│   └── review-sample/          # Example review session
│       ├── input/              # Materials before review (SC, RC, context, artifacts)
│       └── output/             # Results after review (AAR, ADR drafts, summaries, transcripts)
└── runs/                     # Logs of prompt executions and LLM outputs
    ├── backcasting/          # GraphDB backcasting analysis results
    ├── 2025-07-08-sc-001-backcasting.md
    └── 2025-07-08-rc-014-impact.md
```

⸻

🔍 Roles of GitHub in This Toolkit
	1.	External Memory for ChatGPT (AsistA)
→ Documents in docs/for-model/, docs/adr/, shared/ serve as context inputs
	2.	Architecture Repository (Review Targets)
→ samples/case-*/adr/, principles/, and prompts/ hold design data to be reviewed
	3.	Review Records (Outcomes)
→ review-log/ stores session-based review records, each with input and output folders enabling traceability, backlog extraction, and potential automation

## 🚀 Key Updates (2025-01-23)

### New 9-Phase Prompt Sequence
- **Phase 6**: Generate Draft Findings - Creates initial findings with "horror stories" to stimulate stakeholder discussion
- **Phase 7**: Discussion Mode - Interactive validation and refinement of draft findings  
- **Phase 8**: Action Extraction - Transforms validated findings into implementation-ready action items
- **Phase 9**: Final Report Generation - Produces stakeholder-specific deliverables (Executive Summary, Action Plan, Traceability Record, Individual AARs)

### Reorganized Template Structure
- **templates/reports/**: New phase-based organization (phase-6/ and phase-9/)
- **templates/legacy/**: Moved deprecated templates for reference
- **Stakeholder-specific outputs**: Executive Summary (business), Action Plan (development), Traceability Record (governance), Individual AARs (architecture teams)

### Enhanced AI Integration
- **prompt-sequence/**: Complete 9-phase workflow for AI-assisted reviews
- **rag-architecture/**: Design for RAG-based automation
- **Structured templates**: Ready for dynamic content generation with placeholder variables

---

## 📋 Notes

- **prompt-sequence/**: Stores the complete 9-phase execution flow and sequence-specific instructions for AI to follow
- **Draft-to-Final Process**: Phase 6 creates discussion drafts, Phases 7-8 refine through stakeholder input, Phase 9 generates final deliverables
- **Full Traceability**: From GraphDB Success Criteria through findings validation to final action items
- **AAR and ADR**: Now generated as part of the `review-log` outputs and Phase 9 final reports, consolidating review outcomes with their inputs for better traceability