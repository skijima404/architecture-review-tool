

# 🧭 Context: Why This Architecture Review Tool Exists

This repository is not the result of a formal requirement analysis.  
Rather, it's an experiment in how far ChatGPT (nicknamed "AssistA") can support architecture design and review work when given proper structure, inputs, and memory.

We call this a product-out initiative — a hands-on exploration of what becomes possible when we stop asking "What do users need?" and instead ask:  
**"If AssistA were my teammate, what kind of working environment would it need?"**

---

## 🎯 What We're Trying to Achieve

- Make AssistA an effective **architecture reviewer**
- Give it **relevant memory**: project decisions (ADR), principles, design intent, and context
- Provide **structured prompts and rubrics** for evaluating design decisions
- Demonstrate how architecture thinking can be supported, not replaced, by LLMs
- Share a reusable, Markdown-first, GitHub-friendly structure for others to try the same

---

## 🧪 Why This Matters (to us)

In real architecture work, most reviews fail not because people lack knowledge —  
but because the **context is lost**:
- "Why did we decide this last month?"
- "What assumptions are behind this structure?"
- "Which principles were we following?"

By documenting those in a form both humans and AssistA can parse, we can:
- Avoid rehashing decisions
- Promote consistency across teams
- Train AI to give higher-quality feedback, informed by *our own thinking*

---

## 🤖 Role of AssistA

This project treats AssistA as:
- A **review partner** that can ask questions, raise risks, or simulate discussion
- A **reader of ADRs and principles**, capable of judging alignment
- A **structured evaluator**, guided by rubrics
- A **teaching assistant**, helpful in skill assessment for architects

But none of this works unless:
- The inputs are clear
- The knowledge is persistent
- The prompts are consistent

Hence, this repository.

---

## 📦 Why GitHub?

GitHub acts as:
1. **External memory** for AssistA  
2. **Architecture Repository** for designs to be reviewed  
3. **Review Log** for capturing insights and decision history

All in a structure that's:
- Friendly to Obsidian/VSCode
- Forkable and reproducible
- Open to future automation

---

## 🚧 Status

This is a work-in-progress.  
We're still testing, tweaking, and figuring out what a good AI-augmented review process looks like.  
But we're documenting everything here, so you (or future us) can build on it.

---

## ✏️ Related Ideas and Inspirations

- Inception Deck (Agile)
- Architecture Decision Records (ADR)
- Pair programming with AI
- Skill assessment frameworks for architects