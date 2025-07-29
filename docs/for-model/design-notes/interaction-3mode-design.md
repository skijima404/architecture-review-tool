# 🤖 3-Mode Design for AI-Assisted Architecture Review

This document explains the design rationale and expected behavior of the three core interaction modes that follow the initial report generation.

---

## 🎯 Purpose

Enable human-AI collaboration to move from insight to action, with traceable reasoning and decision structures.

These modes appear after the initial report generation phase (Step 6), allowing deeper engagement with findings.

---

## 🧱 Mode Overview

| Mode | Purpose | Typical Input | Output | Transition |
|------|---------|---------------|--------|------------|
| **7. Discussion Mode** | Explore WHY / WHAT IF / SO WHAT based on findings | Prioritized Findings | Clarified assumptions, logical framing | → Action Extraction or Detail Report |
| **8. Action Extraction Mode** | Translate discussion into actionable TODOs | Clarified decisions | `action-items.md` per finding | → Detail Report or back to Discussion |
| **9. Detail Report Triggering** | Deep dive or formalize key issues requiring explanation | High-impact Actions | `report-output-summary.md` entries | → Discussion (for presentation) or back to Actions |

---

## 🔁 Transition Pattern

These three modes do not follow a strict linear order. Users may:

- loop between Discussion and Action as understanding evolves
- trigger Detail Reports when clarity or organizational alignment is needed
- return to Discussion after reviewing Detail Reports with stakeholders

This non-linear flow mirrors the way architects work in real projects.

---

## 📂 Implications for File & Template Structure

Each mode produces structured output tied to the same set of findings:

- `report-output-summary.md` (per finding) → detailed explanation
- `action-items.md` (per finding or per review) → TODO list with optional ADR references
- `adr/` folder → markdown-based decision records with `Status: New`

Example action item block:

```markdown
### 🔧 Action Items for: SaaS属性追加制限

- [ ] Document list of tables where attribute addition is discouraged
- [ ] Draft ADR: `adr/2025-07-XX-attribute-policy.md` (Status: New)
```

---

## 🧠 Design Notes

- These modes are implemented as *prompt modes* rather than fixed steps
- They are meant to support real-time, iterative reasoning between humans and AI
- Supports traceability and accountability in architecture decision-making

