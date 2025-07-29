# Prioritized Findings Summary

## Overview

<Write 1–3 sentences describing structural patterns or common risks observed in this architecture.  
You may refer to common anti-patterns, platform constraints, or long-term consequences.  
Example: “Frequent attribute extension on API-bound objects may lead to post-release UI latency.”>

This table summarizes the key findings from the architecture review.  
Findings are sorted based on estimated impact on business outcomes, alignment with success criteria, and urgency relative to project milestones.

This table is intended to give the reviewee and stakeholders an overview of the issues that require attention, and to support prioritization and planning discussions.

---

## Table of Findings

| ID     | Title                                  | SC Impacted | Priority | Phase to Address | Root Cause ID |
|--------|----------------------------------------|-------------|----------|------------------|----------------|
| F-001  | Retry logic missing in API gateway     | SC-002      | High     | D (System Design) | rc-007         |
| F-002  | Observability ownership unclear        | SC-005      | Medium   | E (Deployment)    | rc-014         |
| F-003  | Inconsistent interface definitions     | SC-003      | Low      | C (Logical Design)| rc-021         |

---

## TOGAF Coverage Summary

Use this table to indicate which architectural views have been sufficiently covered at each TOGAF phase.  
This helps identify blind spots and skill biases in the current architecture documentation.

| Phase | System-Level | Subsystem Interface | Subsystem Internal |
|-------|--------------|---------------------|---------------------|
| B     | <e.g., ✅ To-Be only> | <e.g., ❌ Missing> | <e.g., ❌ Missing> |
| C     | <e.g., ✅ As-Is only> | <e.g., ✅ To-Be only> | <e.g., ❌ Missing> |
| D     | <e.g., ✅ Both> | <e.g., ✅ Both> | <e.g., 🔶 Partial> |

---

## Notes

- **SC Impacted**: The Success Criteria affected by the issue, typically derived via symptoms from the root cause.
- **Priority**: Based on business impact, urgency, and potential stakeholder visibility. Should be reviewed by a human.
- **Phase to Address**: Based on TOGAF phases, ideally where this issue should be mitigated.
- **Root Cause ID**: Corresponds to entries in the GraphDB for traceability.