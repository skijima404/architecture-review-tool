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
