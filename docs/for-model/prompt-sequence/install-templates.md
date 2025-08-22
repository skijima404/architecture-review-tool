# Install Output Templates (Prompt 2)

## Purpose
Establish **awareness of available templates** for draft (Phase 6) and final (Phase 9) outputs without overloading memory. Templates will be loaded just-in-time during actual report generation phases to ensure accuracy and prevent information loss.

---

## Design Principles
- **Just-in-Time Loading**: Templates loaded when actually needed to prevent memory overload
- **Draft vs. Final**: Phase 6 templates are explicitly provisional; Phase 9 templates are stakeholder-ready
- **Stakeholder-Specific**: Final templates serve different audiences (business, technical, governance)
- **Template Awareness**: Know what's available without storing detailed structures

---

## Template Inventory Overview

### Phase 6: Draft Templates
**Available for draft findings generation:**

#### 1) Draft Findings Table
- **Purpose**: Initial findings with horror stories to stimulate stakeholder discussion
- **Location**: `templates/reports/phase-6/draft-findings-table.md`
- **Key Features**: Horror story overview, discussion starting points, explicit draft status
- **When to Load**: During Phase 6 execution

### Phase 9: Final Deliverable Templates  
**Available for final report generation:**

#### 2) Executive Summary
- **Purpose**: Business-focused overview for leadership and stakeholders
- **Location**: `templates/reports/phase-9/executive-summary.md`
- **Target Audience**: Business leadership, project sponsors, decision makers
- **When to Load**: During Phase 9 execution

#### 3) Action Plan
- **Purpose**: Implementation-ready task breakdown with ownership and timelines
- **Location**: `templates/reports/phase-9/action-plan.md`
- **Target Audience**: Development teams, project managers, technical leads
- **When to Load**: During Phase 9 execution

#### 4) Traceability Record
- **Purpose**: Success Criteria → findings → actions mapping with full audit trail
- **Location**: `templates/reports/phase-9/traceability-record.md`
- **Target Audience**: Architecture governance, audit teams, future reviewers
- **When to Load**: During Phase 9 execution

#### 5) Individual AAR  
- **Purpose**: Detailed advisory record for each finding, convertible to ADR when decisions are needed
- **Location**: `templates/reports/phase-9/individual-aar.md`
- **Target Audience**: Architecture teams, decision makers, future reviewers
- **When to Load**: During Phase 9 execution (one AAR per finding)

---

## Just-in-Time Template Loading Flow

**Phase 2**: Establish template awareness and locations (this phase)
**Phase 6**: Load `draft-findings-table.md` when generating draft findings
**Phase 7-8**: Work with draft content, no additional templates needed
**Phase 9**: Load specific final templates based on user requests:
- Executive Summary for business stakeholders
- Action Plan for implementation teams  
- Traceability Record for governance needs
- Individual AARs for each validated finding

---

## Template Storage Structure

```
templates/reports/
├── phase-6/
│   └── draft-findings-table.md
└── phase-9/
    ├── executive-summary.md
    ├── action-plan.md
    ├── traceability-record.md
    └── individual-aar.md
```

**Access Pattern**: Templates will be read from these locations during their respective execution phases, not stored in AI memory.

---

## Key Benefits of Just-in-Time Loading

- **Reduced Memory Overload**: Avoid storing large template structures unnecessarily
- **Accuracy**: Templates are read fresh when needed, reducing staleness
- **Flexibility**: Can load only the specific templates required for each use case
- **Maintainability**: Template updates don't require re-installing in AI memory

## Implementation Notes

- **Phase 6**: Will execute `read_file templates/reports/phase-6/draft-findings-table.md` when generating draft findings
- **Phase 9**: Will execute `read_file` for specific templates based on stakeholder needs (including individual AAR template for each finding)
- **Template Structure**: All templates include placeholder variables ({{ }}) for dynamic content insertion
- **Draft vs Final**: Phase 6 templates explicitly communicate provisional status; Phase 9 templates are stakeholder-ready deliverables

## Confirmation

✅ **Template awareness established**  
✅ **Storage locations identified**  
✅ **Just-in-time loading strategy confirmed**  
✅ **Ready to proceed with architecture input collection**