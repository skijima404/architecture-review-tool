# 🧩 MVP2: RAG-Based Architecture Review Engine

This document defines the second Minimum Viable Product (MVP2) of the Architecture Review Tool initiative.

While MVP1 validated the hypothesis that structured inputs (e.g., Backcasting Map) enable ChatGPT to perform meaningful architecture reviews, MVP2 aims to operationalize this into a repeatable and error-resistant system via RAG (Retrieval-Augmented Generation).

## ✅ MVP2 Goals

- Enable a working review system that uses:
  - Structured architecture knowledge (Graph, YAML, Markdown)
  - Prompt templates
  - RAG to deliver consistent review quality
- Eliminate common human errors in prompt construction and data selection
- Demonstrate practical feasibility through CLI or notebook execution
- Prepare for future UI/demo integration

## 🎯 Why RAG?

- Prevent human error in node selection and prompt handling
- Accelerate review turnaround with reusable components
- Maintain reasoning explainability via prompt templates
- Align with future integration targets (e.g., NotebookLM)

## 🛠️ Core Components

- Prompt templates in `templates/prompts/`
- Node and edge definitions (YAML and CSV)
- Graph traversal logic (backcasting, roll-up)
- Lightweight vector store or retrieval logic
- Execution harness (e.g., CLI or notebook)

## 🗺️ Planned Stages

1. Define RAG architecture (Mermaid or UML)
2. Build a minimal runner that reads a prompt template and node ID
3. Implement retrieval of relevant nodes and relationships
4. Assemble and invoke prompt via ChatGPT
5. Validate results and reviewability
6. Package for demo or guided use

## 📦 Output Artifacts

- `mvp2-rag-architecture.md` (this document)
- `templates/prompts/*.yaml`
- `rag-runner/` or `notebooks/rag-review-*`
- RAG architecture diagram
- Example usage logs

---

MVP2 will determine how far we can go toward practical, structured, and explainable architecture review using AI and a well-curated knowledge base.