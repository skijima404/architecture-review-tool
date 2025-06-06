# Architecture Review Axes

This document organizes the perspectives of architecture reviews using two axes: **Impact Scope** and **Depth of Evaluation**. It aims to support structured understanding and visualization before conducting architecture reviews.

## 1. Overview

Architecture reviews are not checklist-based inspections from a single viewpoint. Instead, they involve multiple dimensions as follows:

### Impact Scope (What aspects are affected by architectural decisions?)

* Development Aspect
* Delivery & Deployment Aspect (CI/CD, release, observability, runbook ownership)
* Operability & Resilience (monitoring, DR, Day 2 operation, recoverability)
* Business Alignment
* Project Feasibility
* Organizational & Team Fit
* Contractual & Procurement Alignment
* Continuous Improvement & Knowledge Management
* Security Alignment

### Depth of Evaluation (How deeply do we assess?)

* Surface Level
* Structural Design Level
* Intent & Rationale Level
* Outcome-Oriented Level

These are presented in a matrix below.

## 2. Architecture Review Matrix

| Impact \ Depth | Surface Level | Structural Design Level | Intent & Rationale Level | Outcome-Oriented Level | Risk Examples When Missed |
|----------------|---------------|--------------------------|--------------------------|-------------------------|-----------------------------|
| Development Aspect | Diagram inconsistencies, naming misalignment | Responsibility misplacement, excessive coupling | Unclear rationale for technology choices | Misalignment with developer experience or team structure | Rework during implementation, accumulation of technical debt |
| Delivery & Deployment Aspect | Incomplete CI diagrams, misunderstood topology | Lack of redundancy, poor observability, missing throttling or failover design | Design incompatible with DevOps or Site Reliability practices | Poor MTTR, lacking observability metrics | Production failures, release delays |
| Operability & Resilience | No runbook or unclear alerts | Missing failover path, no DR topology | No ownership for Day 2 ops or maintenance structure | Poor MTTR, system fails after failover, unclear escalation paths | DR failure, incident escalation delays, post-release operation collapse |
| Business Alignment | Misalignment between slides and architecture diagrams | Missing traceability to KPIs or NFRs | Disconnect with mid-term plans or business strategy | Execution architecture does not realize stated business vision | Inability to justify to executives, failed investment |
| Project Feasibility | Inconsistent documentation granularity | Low modifiability, rigid architecture | Ambiguous scope and stakeholder misalignment | Underlying cause of schedule or budget overruns | Delays, scope creep |
| Organizational Fit | Unclear ownership boundaries | Operations reliant on key individuals | Misalignment with training and support capabilities | Black-box systems, high personnel dependency | Failed transition to operations, fragile maintenance |
| Contract & Procurement | Misalignment between contracts and system architecture | Role and responsibility inconsistencies | Incompatibility with subcontracting or vendor model | Unclear risk allocation and accountability | Contract breaches, blame shifting |
| Continuous Improvement & Knowledge Mgmt | Lost design rationale, lack of review history | Incomplete ADRs, no trace of trade-offs (e.g., flexibility vs. maintainability) | No formalized review perspectives or design agreements | Poor knowledge base or repository | Hard to re-review, no room for iterative improvement |
| Security Alignment | Unclear security requirements | Ambiguous authN/authZ, missing threat modeling | No rationale for privacy or data protection posture | Inability to explain during critical incident | Data breaches, compliance violations, loss of trust |

## 3. Usage Recommendations

* Before a review, clarify which impact areas and how deep the evaluation will go using this matrix.
* If input documents are missing, document the “unreviewable cells” and treat them as known risks.
* Use this matrix to detect imbalance (e.g., too much focus on "Surface-Level Development Aspect") and encourage broader review coverage.

## 4. Future Applications

This framework can be extended to:

* Markdown-based review templates
* Integration with Obsidian or GitHub to manage review history and versioning
* Foundation for AI-assisted review automation using tools like ChatGPT

## 5. Design Principles Behind the Matrix

This structure is based on the following principles:

- **Impact Scope (Horizontal Axis)**: Covers the breadth of influence from development to business, from lifecycle to procurement— including deployment responsibility and Day 2 operability—aligned with TOGAF ADM phases B to G.
- **Depth (Vertical Axis)**: Defines review layers from superficial errors to strategic intent and business alignment. The deeper layers emphasize consistency between business goals and design rationale.
- **Risk-Based Justification**: Each cell includes an example risk to help reviewers understand the importance of each aspect and drive meaningful discussion.
- **Extensibility**: The matrix is adaptable—add/remove axes or weight certain areas depending on project type and organizational maturity.

This matrix shifts architecture review from subjective “gut checks” to structured decision support. When combined with phase-specific TOGAF review designs, it strengthens the coherence and timing of architectural validations. See [TOGAF Review Guide](./togaf-review-guide.md) for further details.


## 6. Maturity Model Perspective

The Architecture Review Axes matrix can also serve as a Maturity Model to assess and improve how architecture reviews are conducted. This perspective helps organizations track their review practices' growth over time and establish goals for improvement.

| Perspective | Initial (Level 1) | Developing (Level 2–3) | Advanced (Level 4–5) |
|-------------|-------------------|-------------------------|------------------------|
| **Impact Coverage** | Focus only on Development Aspect | Includes Delivery and Organizational Fit | Covers full lifecycle including Contracts and Knowledge Management |
| **Depth of Evaluation** | Surface-level checks | Structural and Intent-level reviews | Outcome-driven evaluation aligned with business goals |
| **Documentation & Knowledge** | Scattered documentation | Review records exist but not reused | Structured, reusable formats with ADR integration |
| **Tooling Integration** | Manual reviews only | Partial template use | AI-assisted reviews using structured prompts |
| **Stakeholder Alignment** | Reviewer-dependent | Some consensus on scope | Review scope defined and aligned using this matrix |

This perspective allows you to set improvement targets, such as “Let’s advance from Level 2 to Level 3 by introducing traceable ADRs and business-aligned outcome evaluations.” It is also helpful when evaluating a team’s architectural governance maturity.
