# 🧾 Architecture Advisory Record (AAR) — Design Note

This document defines the concept of the Architecture Advisory Record (AAR), a lightweight but structured way to capture architectural recommendations that do not fit neatly into traditional ADRs.

---

## 🧠 What is an AAR?

An **Architecture Advisory Record (AAR)** is a structured recommendation from architects or technical leads that:

- Does **not mandate** a technical decision like an ADR
- Addresses **project processes**, **quality strategies**, or **design practices**
- Can influence architecture but isn't limited to system components

---

## 📐 Why not use an ADR?

While ADRs are suited for finalized architectural decisions (e.g., "Use OAuth2", "Adopt Kafka"), many valuable insights from experienced architects fall into a gray area such as:

- Suggesting Contract-First design over code-first APIs
- Recommending Test Pyramid restructuring
- Advising improvement of CI/CD pipeline quality gates

These deserve to be documented, reviewed, and traceable — but may not lead directly to an architectural "choice".

---

## ✍️ AAR Template

```markdown
# AAR-XXXX: {Title of the advisory}

## Status
Proposed | In Review | Accepted | Deprecated

## Category
Process | Quality | Practice | Risk | Communication

## Context
Brief description of the current situation or background

## Advisory
The recommendation being made (should be directive and clear)

## Rationale
Why this recommendation is useful in this context

## Impact
Expected impact if the recommendation is followed

## Additional Info
References, metrics, related documents, stakeholders

## Decision (optional)
If promoted to ADR or formally adopted, record rationale here

## Implication (optional)
Any follow-up actions, risks, or changes this advisory leads to

---

## 📚 Usage

- Store AARs in a dedicated folder such as `aar/` or `advisories/`
- Reference AARs from architecture review outputs, especially in Action Items or Discussion summaries
- Use the `Status` field to track the lifecycle of an advisory (e.g., Proposed → Accepted → Deprecated)
- Promote to a full ADR when the advisory becomes a formal architectural decision

---

- 

## 🔮 Realistic Consequence as "Architectural Forecasting"

A key strength of AARs is their ability to document not just abstract reasoning, but *practical foresight*—what is likely to happen if this recommendation is ignored.

This is especially valuable in scenarios where:

- The issue has not yet manifested, but shows signs of risk
- A similar failure has occurred in another project or context
- The audience underestimates the impact without a compelling narrative

We call this a **"realistic consequence"** or "architectural fortune-telling"—backed by historical experience, not guesswork.

### Example:

> In a past multi-vendor project, a lack of Git integration cadence led to a flood of last-minute bugs and a delayed release. This AAR exists so we never let that happen again.

Future implementations may link these sections to an internal *Failure Forecasting DB* or *Reference Class* index.

---

## ✅ Benefits
- Provides a structured channel for non-technical but architecture-impacting insights
- Complements ADRs by covering process and practice guidance
- Supports knowledge transfer and junior architect training