# Prompt Sequence: Collect Architecture Inputs

This document defines the prompt that instructs the user to submit relevant architecture materials needed for the review process.

---

## Purpose

Before triggering the output phase, the AI requires a clear understanding of the system under review. This prompt helps gather all relevant materials and encourages the user to submit them in a structured manner.

---

## Role

The AI remains in its “exploratory” role, actively interpreting inputs, asking clarifying questions, and preparing the foundation for deeper analysis.

---

## What the AI Should Ask For

- Architecture diagrams (component diagrams, sequence diagrams, infrastructure diagrams)
- Architecture principles or guiding styles (e.g., monolith vs microservices, event-driven)
- Building block descriptions (component responsibilities, interfaces, technology choices)
- Constraints and non-functional requirements (performance, availability, corporate policies)
- Any TOGAF-related deliverables or milestones already available

If not all materials are available, partial submissions are acceptable. The AI is expected to:
- Ask clarifying questions
- Identify missing but valuable inputs
- Adapt its approach based on what’s given

---

## Prompt to Trigger This Phase

Prompt: Collect Architecture Inputs

---

## Notes

- This prompt is designed to initiate an architecture information handoff, especially in a multi-turn review session.
- The AI should remain inquisitive and not switch to output mode until explicitly triggered by the next prompt.
- The richness of this input phase significantly affects the quality of the final review output.
# Prompt Sequence: Collect Architecture Inputs (Prompt 3)

This document defines the **requirements** for the prompt that asks the user to submit the **minimum** architecture context needed to proceed to **Prompt 4: Inject GraphDB Review Targets**.

---

## Purpose
Reduce input burden while avoiding misalignment. Collect a **bird’s‑eye** view and a small set of mandatory facts so the review can be anchored on a single Success Criteria (SC) in the next step.

---

## Role & Scope
- **Mode**: Intake / Exploratory (no findings, no prioritization)
- **Scope Lock**: Do **not** generate Findings, Actions, AAR/ADR, or any Prompt 6–9 outputs.
- **Outcome**: A concise `light-collect.md` artifact that downstream prompts can consume.

---

## What the AI Should Ask For (Light Collect — Standard)
Request only the following **minimum** items; placeholders are acceptable if unknown. If the diagram is missing, ask for **Mermaid**; if Mermaid is hard, accept a short textual description.

1) **Architecture Diagram (bird’s‑eye)**  
   - System Context or Container level (C4相当)  
   - File/link or Mermaid snippet accepted

2) **Business Goal (1–2 lines)**

3) **Scope Boundary**  
   - In / Out of scope (bullets OK)

4) **Stakeholders (roles only)**  
   - e.g., Product Owner, Lead Architect, Ops

5) **Top‑3 Non‑Functional Priorities**  
   - e.g., Availability, Operational Load, Compliance

6) **Top‑3 Constraints**  
   - e.g., Cloud/vendor lock, legacy DB must stay, budget/HC limits

7) **(Optional) TOGAF/Phase Info**  
   - Current phase or gate, if known

**Ask minimally:** If any item is missing, ask **one** short follow‑up per turn. Do not escalate the information demand.

---

## Outputs (Artifacts & Locations)
Create the following lightweight artifacts under the active review folder:

- `review-log/<review-id>/input/light-collect.md`
  ```yaml
  review_id: <review-YYYYMMDD-xx>
  date: <ISO8601>
  phase: <optional>
  scope: <free text or bullets>
  stakeholders: [<role1>, <role2>]
  nfr_top3: [<nfr1>, <nfr2>, <nfr3>]
  constraints_top3: [<c1>, <c2>, <c3>]
  diagram_refs: [<path-or-link>]
  assumptions: []
  links: []
  ```
  - Body: short sections mirroring the above (1–3 lines each).

- Store uploaded files/diagrams under:  
  `review-log/<review-id>/input/artifacts/`

- **Gaps List for Prompt 5/5a**  
  Create/refresh a simple list of missing data to drive Clarification/Deep Collect:  
  `review-log/<review-id>/input/gaps.md`

---

## Handoffs
- **To Prompt 4 (Inject GraphDB Review Targets):**  
  Provide `light-collect.md` and **propose or confirm a single SC** anchor if available. The Inject step will expand to "all directly connected dependencies" from that SC (no depth beyond immediate connections).
- **To Prompt 5 (Clarification) / 5a (Deep Collect):**  
  Provide `gaps.md` as the question source. Clarification answers will later be merged into a consolidated **Deep Collect** artifact.

---

## Guardrails
- Do **not** invent new SC/RC/RF/IDs.  
- Do **not** assign priorities or produce action items.  
- Keep outputs **short**; this is an intake step, not a report.

---

## Acceptance Criteria
- `light-collect.md` exists with the **frontmatter keys** above (values may be placeholders).  
- At least **one** diagram reference (file, link, Mermaid, or textual description).  
- `gaps.md` exists if anything is missing; otherwise note `no gaps`.

---

## Notes
- This prompt is intentionally minimal to keep the session moving.  
- Heavy collection happens only if needed in **Prompt 5a: Deep Collect**.