# Architecture Review Tool

This repository contains a modular framework and supporting assets for conducting architecture reviews with the assistance of language models (LLMs) such as ChatGPT.

The tool is designed to support layered review structures, integrate structured reasoning via graphs (e.g., Neo4j), and facilitate human-AI collaboration in both enterprise and project-level architecture assessment.

---

## Goals

- Support structured, repeatable architecture reviews
- Enable reuse of reasoning patterns across projects and organizations
- Provide LLMs with contextually rich data for reasoning and generation
- Foster skill development through simulation-based assessments

---

## Repository Structure

```
docs/
│
├── for-model/                  # Knowledge and structure for model-driven interaction
│   ├── usage-guides/          # Guides on how to use this repository
│   ├── design-notes/          # Architectural structure and review methodology
│   ├── context.md             # Purpose and goals of this project
│   └── llm-threshold-notes.md # Why general-purpose LLMs are used
│
├── for-humans/                # Human-readable guides and usage instructions
│
├── adr/                       # Architecture Decision Records (for this tool itself)
│
└── ...                        # (Additional code, data, or review scenarios)
```

---

## Status

This project is under active development. Feedback and collaboration are welcome.

---

## Related Repository

- [architecture-review-knowledge](https://github.com/skijima404/architecture-review-knowledge)  
  Contains shared architecture knowledge, reusable reasoning patterns, success criteria trees, and root cause definitions.  
  Designed to be used as a reference model or knowledge base alongside this review tool.
