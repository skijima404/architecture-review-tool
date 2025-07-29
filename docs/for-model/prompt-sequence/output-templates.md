# Output Templates

This step installs the output format templates that the architecture reviewer assistant will use when generating summaries and recommendations.

## Purpose

Ensure a consistent and structured format for outputs, enabling human stakeholders to easily understand and take action based on the findings.

## Components

The following templates are loaded at this stage:

### 1. Prioritized Findings Table

- A ranked list of issues, root causes, or architectural risks, annotated with:
  - `Root Cause` title
  - `Phase to Address`
  - `Priority`
  - `Optional: TOGAF Coverage`, if applicable
- May include a short narrative summary (overview) to guide attention and interpretation.

### 2. Output Summary Template (per finding) [Optional, up to 5 items per request]

- Structured insight per individual item in the findings table, generated upon request for a limited number of high-priority items.
- Includes:
  - Title (normally aligned with the Root Cause from the GraphDB)
  - Description
  - Risk & Impact
  - Phase to Address
  - Suggested Actions

## Notes

- The templates do not include TOGAF Coverage Summary anymore; this is handled separately.
- The assistant should fill these templates when prompted via `Trigger Report Generation Mode`.
