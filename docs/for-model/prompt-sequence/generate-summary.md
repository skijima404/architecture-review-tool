# Prompt Sequence: Generate Prioritized Architecture Review Summary

This document describes the purpose and behavior of the `Generate Prioritized Architecture Review Summary` prompt, which triggers the output mode after an architecture review session has been completed.

---

## 🧠 Role Transition

Once the review phase is finished, the AI transitions from an "explorer" role (digging through findings and asking questions) into a "reporting assistant" role.

This prompt acts as the trigger for that transition, allowing the AI to switch into output-generation mode.

---

## 🎯 Objective

The AI is expected to generate a structured report based on the findings gathered during the review session. The report is intended for human stakeholders, including technical and non-technical roles.

The report should be:
- Concise and easy to read
- Actionable and prioritized
- Structured according to the output template

---

## 📦 Inputs Expected Before Triggering

- Architecture materials (e.g., diagrams, component specs)
- Review axes definitions (Operational / Structural / Business)
- GraphDB-derived Backcasting Map (Success Criteria, Symptoms, Root Causes)
- Clarification or dialogue that preceded the findings
- Output summary format (template)
- Optional: Additional constraints or project context

---

## 📝 Report Contents

After receiving this prompt, the AI should generate the following sections:

1. **Overview**
   - Summarize common themes, risk patterns, or emerging trends.
   - Offer a brief narrative or "fortune telling" based on architecture design choices.

2. **Prioritized Findings Table**
   - Each entry includes:
     - Root Cause ID and title
     - Mapped Success Criteria
     - Suggested Phase to Address (aligned with TOGAF)
     - Priority (Low / Medium / High)
   - The order should reflect urgency and impact.

3. **TOGAF Coverage Summary**
   - Identify gaps or unaddressed areas in the required TOGAF deliverables.
   - Example categories: Architecture Vision, Business Architecture, Information Systems Architecture, Technology Architecture, Opportunities & Solutions, Implementation Governance.

---

## ✅ Output Format Location

The structure of the report is defined in:

```
/workspace/architecture-review-tool/templates/prioritized-findings-table.md
```

The AI must use this format when producing the summary.

---

## 💡 Notes

- This prompt is only used after the review session has completed.
- Users may choose to delay triggering this prompt to continue clarification or deeper questioning.
- The generated summary is typically followed by a human review and prioritization confirmation before final delivery.

```
Prompt: Generate Prioritized Architecture Review Summary
```

---
