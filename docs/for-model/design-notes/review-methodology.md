# Architecture Review Methodology: From Axes to Actionable Feedback

This document outlines a practical and philosophy-driven methodology for conducting architecture reviews that lead to prioritized, actionable outcomes. It is based on years of experience in operational troubleshooting and enterprise architecture advising.

---

## 1. Philosophy

A good system is one that:
- Avoids failures
- Continues to meet user needs over time

This methodology focuses on identifying risks that threaten business continuity and long-term adaptability, and translating architectural insights into concrete, time-bound actions.

---

## 2. The Three-Step Review Framework

### Step 1: Broad Scan via Review Axes

- Use high-level axes (Operational, Structural, Business Fit) to quickly identify areas of concern.
- This stage focuses on **coverage**, not depth.
- Example questions:
  - "What happens if this system stops?"
  - "How complex is this part to maintain or reason about?"

### Step 2: Prioritization via Backcasting Map

- Connect Success Criteria → Symptoms → Root Causes
- Structure concerns as causal chains, not isolated findings
- Identify areas where understanding is shallow, and define follow-up review focus

### Step 3: Action Planning via Milestone Alignment

- Use TOGAF phases and project milestones to determine when action must be taken
- Sort findings by:
  - Criticality to Success Criteria
  - Long-term impact
  - Visibility to stakeholders (reputation risk)
  - Uncertainty and controllability
- Deliver results as:
  - Ranked finding list
  - Backcasting map annotated with TOGAF phases and deadlines
  - Coverage matrix of TOGAF deliverables

---

## 2.5 Dialog, Reflection, and Structural Sensitivity

Architecture review is not merely about critique or validation—it is a structured dialogue.  
In this dialogue, the reviewer poses questions not to judge, but to surface assumptions, highlight blind spots, and invite reflection. The reviewee is encouraged to re-express their design decisions through another's lens, often leading to deeper insights and improved clarity.

This reflective process is essential because architecture is inherently sensitive to change. Like a game of Jenga, modifying one piece can destabilize others.  
Local changes in architecture often have system-wide implications: introducing microservices may imply container orchestration and observability tooling; adopting DevOps may necessitate Agile practices to maintain effectiveness.

A meaningful review, therefore, does not merely examine isolated design fragments—it anticipates and interrogates their ripple effects. It helps the team not only see what was changed, but also what must change with it.

## 3. Closing Thoughts

Architecture review is not the goal in itself—it is a means to improve system quality and ensure alignment with long-term business needs. The ultimate purpose of any review is to identify actionable insights that lead to meaningful improvements. A successful review process enables stakeholders to prioritize efforts, reduce future risks, and build systems that are not only technically sound but also resilient, adaptable, and valuable to the organization.