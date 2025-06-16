# 🧠 When Would We Need a Custom LLM?

This document captures an open question driving this experiment:  
**At what point does AssistA (ChatGPT) cease to be sufficient for architecture review work, requiring a dedicated/custom LLM instead?**

---

## ✅ Advantages of a Custom LLM

- Purpose-specific training and terminology alignment
- Ability to keep proprietary data fully private
- Potential for tighter integration with internal systems

---

## ❌ Downsides of a Custom LLM

- High cost of data curation and fine-tuning
- Maintenance overhead (updates, concept drift)
- Less interactivity or general-purpose adaptability
- ChatGPT currently bypasses many of these with general reasoning and strong promptability

---

## 🔍 The True Boundary (and Why We're Testing It)

This project is not trying to replace AssistA — it's trying to see **how far we can go before replacing it becomes necessary**.

Key factors:
- Can humans provide context summaries effectively enough?
- At what scale does the architecture context (ADRs, decisions, rationale, constraints) exceed AssistA’s working memory?
- Does review quality degrade due to token limits or due to poor input?

---

## 🧪 Current Position

> We’re not blocked by AssistA’s intelligence — we’re bottlenecked by **how well humans describe what we’re designing**.

So far:
- Rich, structured inputs yield meaningful review output.
- Missing context leads to shallow, generic feedback — a reflection of poor inputs, not model capability.

---

## 🗺️ This Is the Real Experiment

We are not evaluating ChatGPT’s limits.

We are evaluating:
- The *design documentation practices* needed to make LLMs effective reviewers.
- The *moment* we would need to switch to an internal or extended model.

*Until then — AssistA is not the limit. We humans are.*