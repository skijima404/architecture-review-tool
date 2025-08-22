# Generate Draft Findings (Phase 6)

This document defines the purpose and behavior of the **Generate Draft Findings** prompt, which creates initial findings to stimulate stakeholder discussion and validation.

---

## 🧠 Role Transition

The AI transitions from **information gathering** (Phases 1-5) into **initial synthesis** mode. This is explicitly a **draft phase** - the AI creates preliminary findings to kickstart stakeholder engagement, not final conclusions.

The AI should maintain an **exploratory mindset** while organizing gathered information into discussable findings.

---

## 🎯 Objective

Generate preliminary architectural findings that serve as **discussion catalysts** rather than definitive assessments. The output should:

- Highlight potential concerns and risks clearly
- Present findings in a format that invites stakeholder feedback
- Include "horror story" scenarios to stimulate engagement
- Explicitly communicate the draft nature of all conclusions

---

## 📦 Inputs Expected Before Triggering

- **Architecture materials** collected in Phase 3 (diagrams, component specs, constraints)
- **GraphDB nodes** injected in Phase 4 (Success Criteria, Root Causes, Symptoms)
- **Clarification responses** from Phase 5/5a (resolved ambiguities, additional context)
- **Draft findings table template** from Phase 2 (skeleton structure)

---

## 📝 Draft Output Contents

After receiving this prompt, the AI should generate:

### 1. **Horror Story Overview**
- Paint vivid "worst-case scenarios" of what happens if architectural issues are ignored
- Focus on business impact and stakeholder consequences
- Use specific, relatable examples rather than generic warnings
- Example: *"Without proper retry logic, a single API timeout could cascade into a 2-hour payment system outage during Black Friday, potentially costing $500K in lost sales..."*

### 2. **Draft Findings Table**
Follow the structure from `templates/phase-6/draft-findings-table.md`:

| ID | Title | SC Impacted | Draft Priority | Root Cause ID | Notes |
|----|-------|-------------|----------------|---------------|-------|
| F-001 | {{ descriptive_title }} | {{ sc_ids }} | {{ high/medium/low }} | {{ rc_id }} | {{ discussion_point }} |

**Required columns:**
- `finding_id` - Unique identifier (F-001, F-002, etc.)
- `title` - Clear, non-technical description of the issue
- `sc_impacted` - Success Criteria IDs threatened by this finding
- `draft_priority` - Initial assessment (explicitly marked as draft)
- `root_cause_id` - GraphDB Root Cause reference for traceability
- `notes` - Questions or uncertainties to discuss

### 3. **Discussion Starting Points**
Generate specific questions to guide stakeholder conversation:
- "Which of these findings surprises you most?"
- "Are there business constraints we haven't considered for F-002?"
- "What timeline pressures might affect the priority of F-005?"

---

## ✅ Template Location

The output structure is defined in:
```
templates/phase-6/draft-findings-table.md
```

---

## 🔄 Expected Follow-up Flow

**After Phase 6:**
1. **Stakeholder Review** - Business and technical teams examine draft findings
2. **Phase 7: Discussion** - Interactive refinement and validation
3. **Phase 8: Action Extraction** - Convert validated findings into actionable tasks
4. **Phase 9: Final Reports** - Generate stakeholder-ready deliverables

---

## ⚠️ Critical Guidelines

### **Draft Mindset**
- **Explicitly state** that all conclusions are preliminary
- **Invite contradiction** and additional information
- **Acknowledge uncertainty** where it exists
- **Avoid final judgments** - this is exploration, not conclusion

### **Engagement Focus**
- **Stimulate discussion** rather than provide answers
- **Surface assumptions** for stakeholder validation
- **Highlight gaps** in understanding that need filling
- **Create urgency** through realistic consequence scenarios

### **Quality Markers**
- Each finding traces back to specific GraphDB nodes (Root Causes, Success Criteria)
- Horror stories are specific and business-relevant
- Discussion questions are actionable and specific
- Uncertainty and confidence levels are clearly indicated

---

## 💡 Example Trigger Prompt

```
Prompt: Generate Draft Architecture Review Findings

Based on the architecture materials collected and GraphDB analysis completed, create draft findings to initiate stakeholder discussion. Include horror story scenarios and specific discussion starting points.

Remember: This is explicitly a DRAFT phase - findings will be refined through discussion before final reporting.
```

---

## 📋 Success Criteria for This Phase

- [ ] Draft findings table populated with 3-7 key concerns
- [ ] Horror story overview includes specific business impact scenarios  
- [ ] Discussion starting points are concrete and actionable
- [ ] All findings trace back to GraphDB nodes for validation
- [ ] Draft nature is clearly communicated throughout
- [ ] Output invites stakeholder engagement rather than presenting conclusions
