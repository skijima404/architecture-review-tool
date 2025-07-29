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