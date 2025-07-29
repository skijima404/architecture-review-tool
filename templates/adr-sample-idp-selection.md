# ADR-SAMPLE-001: Internal Developer Portal (IDP) Requirements and Product Options

## Status
Sample Only

## Context

To support scalable Platform Engineering adoption, we need to define essential capabilities of an Internal Developer Portal (IDP) and identify viable product options that are operationally feasible.

## Desired Capabilities

### Portal UX
- A central entry point for developers with minimal cognitive friction (**Must**)
- Ability to either embed all tools or serve as a gateway to external systems (**Must**)
- Optional: prevent accidental access by non-developer personas (**Could**)

### Service Catalog
- Categorized list of developer self-serviceable components (**Must**)
- Low maintenance overhead for publishing and managing catalog entries (**Must**)
- Execution feedback (success/failure visibility) (**Should**)
- Guardrails for non-developer usage (**Should**)

### Documentation & Search
- Centralized or linkable access to onboarding and guidelines (**Must**)
- Low publishing/maintenance friction (**Must**)
- Cross-document search or alternative navigation aids (**Should**)

### SSO Integration
- Integration with enterprise IdP for user management (**Must**)
- Role/group-based access restriction using IdP metadata (**Could**)

## Product Selection Patterns

- **Pattern A: Integrated IDP Solutions**
- **Pattern B: Composed Point Solutions**

## Candidates (Example Only)
- OSS IDP Platform X
- Self-hosted Git-based Doc Viewer
- Enterprise Workflow Tool Y

## Decision
TBD