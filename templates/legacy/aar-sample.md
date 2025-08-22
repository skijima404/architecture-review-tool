# AAR-0001: Defining Rules for Integration Test Frequency and Git Repository Coordination

## Status
Proposed

## Category
Process | Quality | Practice

## Context
In projects involving multiple vendors or subsystems, integration testing is often postponed until late phases, leading to unexpected failures, misalignments, and quality risks. These issues are typically exposed only after code is merged and deployed in a shared test environment, creating significant downstream impact.

## Advisory
Establish explicit rules and expectations in the RFP regarding:
- The frequency of full-system integration tests (e.g., every 3 months)
- The responsibilities of each vendor for pre-integration validation
- The required cadence for pushing assets into a shared Git repository or artifact hub
- Pipeline expectations and environment readiness for integration

This advisory aims to shift defect discovery earlier (shift-left) and reduce the risk of latent integration failures.

## Rationale
When integration test cadence and asset sharing timing are not clarified, subsystems may evolve in isolation, leading to integration failures late in the cycle. Early alignment promotes transparency, accelerates feedback, and improves delivery confidence.


## Impact
- Earlier defect detection
- Reduced schedule compression in later phases
- Improved coordination between teams
- Clearer vendor responsibilities and delivery expectations

## Realistic Consequence

In a past multi-vendor project, subsystem teams developed in isolation without shared expectations for integration cadence or repository alignment. When the first full integration was attempted near release, over 30 defects emerged, ranging from API mismatches to incompatible data models. The shared test environment was unstable, and no single team had full visibility into the causes. This resulted in emergency triage efforts, a delayed launch, and finger-pointing among vendors — all of which could have been prevented with early alignment and clear contractual expectations.

## Additional Info
- Related to test strategy, DevOps pipeline readiness, and RFP documentation quality
- Can be combined with guidance on test pyramid balance and CI integration

## Decision
N/A (recommendation only)

## Implication
If accepted, update RFP templates to include:
- Integration cadence
- Asset delivery rhythm
- Shared environment expectations
