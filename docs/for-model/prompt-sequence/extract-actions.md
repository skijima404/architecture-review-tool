

# Prompt Sequence: Action Extraction Mode (Step 8)

This document describes the **Action Extraction Mode** (Step 8) in the prompt sequence for the architecture review tool. In this mode, the model is tasked with extracting high-level "actions" from a user's natural language request, which will later be mapped to code transformations or suggestions.

---

## Purpose

The Action Extraction step translates a user's architectural change request (usually in natural language) into a structured list of actions. These actions are used as an intermediate representation to drive downstream code modifications or recommendations.

---

## Input

- **User Request:** A natural language description of the desired change or improvement (e.g., "Refactor all controllers to use dependency injection.").
- **Context:** (Optional) Supporting information such as project structure, code snippets, or prior steps in the prompt sequence.

---

## Output

- **YAML-formatted list of actions**, each with a clear and concise description.
- Each action should be atomic and implementation-agnostic (i.e., not tied to a specific code diff yet).

---

## Example

**User Request:**  
> "Refactor all controllers to use dependency injection instead of directly instantiating service classes."

**Extracted Actions (YAML):**
```yaml
actions:
  - description: Identify all controller classes in the codebase.
  - description: For each controller, detect direct instantiation of service classes.
  - description: Modify controllers to accept service instances via constructor parameters (dependency injection).
  - description: Update service instantiations to be managed by a dependency injection container or framework.
```

---

## Checklist for Action Extraction

- [ ] Each action is a single, high-level step.
- [ ] Actions are not implementation-specific (avoid code or file names unless essential).
- [ ] The list covers the full intent of the user request.
- [ ] Output is formatted as valid YAML under an `actions:` key.
- [ ] Descriptions are clear, concise, and use imperative language.

---

## Notes

- If the user request is ambiguous, include clarifying actions (e.g., "Request clarification on which controllers are affected").
- Do **not** generate code or diffs at this stage—only action descriptions.