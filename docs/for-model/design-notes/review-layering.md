
# Review Structure Layering in Architecture Review

## Background

Architecture reviews cannot be treated as a single monolithic activity. Depending on the perspective, responsibility, and architectural focus, different layers require different review viewpoints.

By organizing review structures into “layers,” we can apply the appropriate focus and criteria to each context, enabling more scalable and reusable review practices.

---

## Definition of Review Layers

| Layer | Reviewee | Reviewer | Focus | Example Outputs |
|-------|----------|----------|-------|------------------|
| EA Vision Level | EA Team | Senior EA / Enterprise-wide EA Board | Success criteria, principle alignment | Success criteria definitions, principle traceability |
| Implementation Project Level | Development Team (or SI) | EA / Solution Architect | Feasibility, adherence to principles, NFR fulfillment | Technology selection validation, NFR design strategies |
| Architecture Style Specific | Development Team | Style Expert (e.g., MSA Reviewer) | Best practices by style | Layering strategy, state handling, API contract guidance |

---

## Examples of Map Separation

- `EA Backcasting Map`:
  - **Subject**: Success Criteria  
  - **Purpose**: Structuring success factors and what threatens them  
  - **Audience**: EA teams, business sponsors

- `Project Implementation Map`:
  - **Subject**: Symptoms / Root Causes  
  - **Purpose**: Risk identification and technical mitigation design  
  - **Audience**: Project teams, implementation architects

- `Style-Specific Review Guide`:
  - **Subject**: Architecture style (e.g., Microservices, Batch processing)  
  - **Purpose**: Clarify architectural guidance by style  
  - **Audience**: Specialist reviewers, technical leads

---

## Key Relationships Between Layers

- `Success Criteria → Symptom`  
  - Represents what threatens a success factor (`threatened_by`)

- `Symptom → Root Cause`  
  - Indicates the underlying issue (`triggered_by`)

- `Root Cause → Mitigation`  
  - Can be linked with `mitigated_by` and other future design nodes

---

## Notes

- Miro maps should be divided by layer to control information density and shift perspectives as needed.
- The GraphDB structure can be separated per layer (e.g., `graph-ea`, `graph-dev`) to support scalability and traceability.
- This layering approach is key to designing sustainable and modular review practices.

---

## Future Ideas

- Create review prompt templates for each layer
- Explore tools to generate Miro templates from GraphDB paths
- Convert architecture style-specific review checklists into GraphDB nodes