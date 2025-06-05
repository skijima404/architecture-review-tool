# TOGAF Phase-Specific Architecture Review Perspective Guide

This document is a guide that organizes representative perspectives and review objectives for architecture reviews conducted at the end of each phase of the TOGAF ADM (Architecture Development Method).

## Phase A: Architecture Vision

- **Review Perspectives**:
  - Clarification of NFRs (Non-Functional Requirements) aligned with the business vision
  - Sufficient concreteness of the concept to support investment decisions
- **Risks to Confirm**:
  - NFRs are defined only as templates and are not linked to the vision
  - The concept is too abstract and disconnected from technical design
- **Supplementary Perspectives**:
  - Are stakeholders' (business, operations, security, etc.) expectations reflected in the architecture principles?
  - Is the scope of the architecture clearly defined (boundary setting)?

## Phases B–D: Business / Information Systems / Technology Architecture

- **Review Perspectives**:
  - Consistency between NFRs and configuration design (performance, availability, modifiability, etc.)
  - Consistency of the technology stack (e.g., reasons for introducing Camel or Kafka)
  - Consistency between development aspects and delivery aspects (ease of development, CI/CD compatibility)
  - Explainable responsibility division (service granularity, clear ownership of data)

- **Supplementary Perspectives**:
  - 🚨 Undefined facade layer (e.g., Camel)
  - 🚨 Lack of old vs. new comparison mechanisms (e.g., Rule Engine)
  - 🚨 Premise environment for parallel operation not prepared
  - 🚨 Lack of structural consistency with test strategy
  - Recognition and explanation of major trade-offs in architecture (e.g., performance vs. flexibility)
  - Security design (authentication, authorization, threat modeling, etc.) considered from the initial stages
  - Effective utilization of standardized technical assets within the organization
  - Incorporation of operational ease (monitoring, alerts, metrics) into the development configuration

## Phase E: Opportunities & Solutions

- **Review Perspectives**:
  - Whether vendor assignments and contract units align with the architecture
  - Whether responsibility boundaries do not conflict with configuration diagrams
  - Whether the solution configuration is neither excessive nor insufficient
- **Supplementary Perspectives**:
  - Whether solution proposals are feasible under budget, resource, and schedule constraints
  - Whether PoCs are conducted as needed and their results are reflected

## Phase F: Migration Planning

- **Review Perspectives**:
  - Validity of migration strategy including strangler pattern
  - Formulation of OCM (Organizational Change Management) and operational system policies
  - Presence of technical support design for environment migration, DB separation, and phased switching
- **Supplementary Perspectives**:
  - Whether business continuity during migration is ensured (risks of downtime and rollback strategies)
  - Inclusion of planning, verification, and rehearsal for data migration

## Phase G: Implementation Governance (First half: Alignment with technical implementation, Second half: Alignment with outcomes)

- **Review Perspectives**:
  - Whether release plans and WBS align with the configuration
  - Whether release order matches dependencies
  - Preparation for handover to operations (log design, observability, failure response design)
  - Whether the implemented configuration contributes to the outcomes and effectiveness indicators set in the Vision
  - Whether mapping between configuration and outcome indicators is possible
  - Whether it contributes to the satisfaction of intended users and stakeholders

- **Supplementary Perspectives**:
  - 🚨 In pre-operation handover reviews, deficiencies in log/monitoring design missed in Phase D are often revealed
  - 🚨 Alignment reviews with implementation sprints are important
  - Whether implementation reviews and guidelines for architecture compliance exist and are operated
  - Whether policies for detecting, recording, and repaying technical debt are clearly stated
  - Whether both quantitative and qualitative indicators are used for outcome evaluation
  - Whether improvement actions are clarified for gaps with the Vision

## Phase H: Architecture Change Management

- **Review Perspectives**:
  - Whether a mechanism for continuous review is incorporated (principally ADR)
  - Integration with the Architecture Repository
  - Whether review perspectives are organized in a format reusable in the future
- **Supplementary Perspectives**:
  - Whether processes for receiving, evaluating, and approving architecture change requests are established
  - Whether principles and rules are maintained through changes (e.g., recording changes and feedback)

## Supplement: Integration with Architecture Review Axes

The phase-specific review perspectives presented in this guide are organized chronologically as viewpoints to be confirmed at milestones along the TOGAF ADM process.

On the other hand, the "Architecture Review Axes" is a supplementary framework that organizes architecture reviews along two structural axes to visualize the comprehensiveness and depth of the review target:

- **Impact Axis** (e.g., development aspects, delivery aspects, business alignment, project progress, organizational fit, contract and procurement alignment, knowledge management, etc.)
- **Depth Axis** (surface level, configuration design level, concept/intent level, outcome-oriented level)

Using this framework together can provide practical benefits such as:

- Organizing which domains and depths each phase's review perspectives correspond to
- Confirming coverage of check points and highlighting key areas
- Establishing a common understanding of the review scope among stakeholders before conducting reviews
- Structuring and reusing review content effectively for recording and knowledge management
- Serving as a foundation for designing review support prompts using tools like ChatGPT

The "Architecture Review Axes" acts as a powerful complementary tool to grasp the perspectives presented in this guide three-dimensionally and to design and conduct review activities more effectively overall.
