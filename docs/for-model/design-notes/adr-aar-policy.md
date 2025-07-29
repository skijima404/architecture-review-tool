# 📘 Policy: Relationship Between AAR and ADR

This document defines the operational relationship between **Architecture Advisory Records (AARs)** and **Architectural Decision Records (ADRs)**, and outlines how they are used collaboratively in the architecture review process.

---

## 🎯 Purpose

To provide a structured, traceable process for managing architectural observations, recommendations, and decisions—without losing context or creating fragmented documentation.

---

## 🧱 Role of AAR and ADR

| Type | Purpose | Ownership | Trigger | Status Lifecycle |
|------|---------|-----------|---------|------------------|
| **AAR** (Architecture Advisory Record) | Suggest improvement, highlight risks, structure architectural insights | Architect or Reviewer | As early as a concern or observation arises | Proposed → In Review → (→ ADR or Accepted) |
| **ADR** (Architectural Decision Record) | Record a finalized architecture decision | Decision owner (typically lead architect or team) | When a formal decision is made and needs to be justified and recorded | Draft → Accepted / Rejected |

---

## 🔄 Operational Flow

1. **Start with AAR**  
   Use AARs to record structured concerns, recommendations, or insights discovered during reviews. This acts as the **backlog of architectural advisory items**.

2. **Promote to ADR if needed**  
   When consensus is reached or a decision is required, an AAR may be promoted into a formal ADR. The AAR can link to the corresponding ADR for traceability.

3. **Review Loop**  
   AARs may remain open or evolve over time. They are useful for documenting ongoing concerns that have not yet reached decision status.

---

## 🧠 Why Use AAR as Backlog?

- Keeps **all architectural concerns in one place**
- Encourages early documentation without the burden of finality
- Supports natural collaboration with GenAI to elaborate, refine, and even propose ADR drafts
- Prevents “decision inflation” (creating ADRs for issues that aren’t yet resolved)

---

## 🔗 Cross-Linking Example

In AAR:
```markdown
## Decision
Promoted to ADR: [ADR-0015: Centralized Logging Design](../../adr/adr-0015.md)
```

In ADR:
```markdown
## Context
Derived from advisory: [AAR-0023: Logging Strategy Gaps](../../aar/aar-0023.md)
```

---

## ✅ Summary

- **Default to AAR** for advisory-level concerns
- **Use ADR** only when a formal decision has been made
- Encourage collaboration and backlog tracking through AARs
- Use both formats to enhance architecture traceability and knowledge reuse
