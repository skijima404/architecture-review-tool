# 🧭 Architecture Review Prompting Sequence

This directory documents the recommended flow for engaging the architecture reviewer assistant using prompts and structured inputs.

---

## 1. Initialize Mode
**Purpose**: Define assistant's role and reasoning context.

```text
You are an architecture reviewer assistant. You support human stakeholders by reasoning over structured architecture information such as Root Causes, Symptoms, and Success Criteria stored in a GraphDB.
```

---

## 2. Install Output Templates
**Purpose**: Provide the assistant with the structure for findings and summaries.

**Files to provide**:
- `prioritized-findings-table.md` – Summary table template
- `report-output-summary.md` – Individual finding deep dive format

> These are provided as Markdown templates so the assistant can generate output in expected structure.

---

## 3. Collect Architecture Inputs
**Purpose**: Supply high-level architecture context and constraints.

**Examples include**:
- Architecture diagrams (as text or image summaries)
- Constraints and non-functional requirements
- TOGAF phase expectations

> Optional phase: until the user is satisfied with context coverage.

---

## 4. Inject GraphDB Review Target
**Purpose**: Provide Success Criteria and related nodes from the knowledge graph for evaluation.

**Data to include**:
- Selected Success Criteria
- Related Root Causes, Symptoms, Risk Factors (as structured node sets or YAML/Markdown)

> Each Success Criteria will trigger localized clarification and review.

---

## 5. Clarification Questions
**Purpose**: Assistant may ask for details required to understand Success Criteria realization conditions.

---

## 6. Trigger Report Generation Mode
**Purpose**: Switch from analysis mode to summarization and reporting.

**Prompt**:
```text
Prompt: Generate Prioritized Architecture Review Summary
```

The assistant will:
- Generate the `Overview` section reflecting holistic insight
- Populate the Findings table
- Optionally suggest TOGAF Coverage Summary if architecture inputs were provided

---

## 📝 Notes
- Step 3 provides global context, Step 4+5 provide local evaluative targets.
- User may iterate in Step 4 as needed to add multiple Success Criteria.
- Each finding in the summary can link to a `report-output-summary.md` entry.

---

## 📚 Next Steps

Once all prompt sequences are documented, consider turning this file into a `README.md` with links to each detailed step:

1. [Initialize Mode](./initialize.md)
   - Define the assistant's role and reasoning context.
2. [Install Output Templates](./install-template.md)
   - Provide Markdown templates for findings and summary output.
3. [Collect Architecture Inputs](./collect-architecture-input.md)
   - Supply high-level architecture context and constraints.
4. [Inject GraphDB Review Target](./inject-graphdb-nodes.md)
   - Provide Success Criteria and related nodes from the knowledge graph.
5. [Clarification Questions](./clarification.md)
   - Assistant may ask for details required to understand Success Criteria realization.
6. [Trigger Report Generation Mode](./generate-summary.md)
   - Switch from analysis to summarization and reporting.
7. [Discussion Mode](./discussion-mode.md)
   - Handles interactive review conversation and refinement of findings, allowing stakeholders and the assistant to discuss findings, clarify ambiguities, and iterate on proposed solutions. This aligns with earlier discussion and supports collaborative review.
8. [Action Extraction Mode](./extract-actions.md)
   - Produces AAR (After Action Review) records, acting as a backlog of issues or findings. These records can later be converted into ADR (Architecture Decision Record) drafts if needed, ensuring findings are actionable and traceable.
9. [Detail Report Triggering](./generate-detail-report.md)
   - Can generate detailed AAR entries or ADR drafts on request, including IDs for Root Causes, Symptoms, and Success Criteria for traceability. This supports deep dives into specific findings or issues as needed.
