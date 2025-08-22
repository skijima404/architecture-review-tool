# Action Extraction (Phase 8)

This document defines the purpose and behavior of the **Action Extraction** phase, which transforms validated findings from stakeholder discussion into structured, implementation-ready action items.

---

## 🧠 Role Transition

The AI transitions from **discussion facilitation** (Phase 7) into **implementation planning** mode. The AI should act as a **project planner** that converts validated insights into concrete, actionable tasks with clear ownership and timelines.

The AI should maintain a **results-oriented, practical mindset** while ensuring every validated finding becomes a trackable action item.

---

## 🎯 Objective

Convert **validated findings from Phase 7** into high-level action categories and areas of focus that can guide subsequent detailed planning. This phase bridges the gap between architectural insights and planning direction.

Key goals:
- **Transform findings into action areas** with conceptual scope and focus
- **Identify action categories** (technical, process, organizational)  
- **Establish relative priorities** based on business impact and dependencies
- **Group related actions** into logical implementation themes
- **Prepare conceptual inputs** for Phase 9 final report generation

---

## 📦 Inputs Expected Before Triggering

- **Validated Findings Summary** from Phase 7 (stakeholder-confirmed conclusions)
- **Priority Adjustments Log** from Phase 7 (business constraint-based changes)
- **New Information** from Phase 7 (additional context discovered during discussion)
- **Outstanding Questions** from Phase 7 (items requiring follow-up)
- **Business constraints and timelines** (budget, resource availability, deadlines)

---

## 🔄 Action Extraction Process

### **1. Finding-to-Action Mapping**
For each validated finding, systematically create action items:

#### **Action Categorization**
- **Group findings** into logical action themes
- **Identify action types** (technical architecture, process improvement, organizational change)
- **Define scope boundaries** (what each action area should address)
- **Establish conceptual outcomes** (what success looks like)

#### **Dependency Identification**
- **Identify logical prerequisites** (what concepts must be addressed first)
- **Note external decision points** (areas requiring stakeholder decisions)
- **Sequence action areas** based on architectural dependencies

#### **Impact Assessment**
- **Categorize by architectural domain** (operational, structural, business alignment)
- **Assess relative complexity** (simple, moderate, complex)
- **Identify affected system areas** (based on C4 model components)

### **2. Action Prioritization**
Using validated findings priorities and business constraints:

#### **Relative Priority Grouping**
- **Critical**: Must address to meet basic success criteria
- **Important**: Significant value with manageable complexity
- **Beneficial**: Good to have when resources allow

#### **Impact-Effort Assessment**
- **High Impact/Low Effort**: Quick wins for early momentum
- **High Impact/High Effort**: Strategic initiatives requiring planning
- **Low Impact/Low Effort**: Consider for future iterations
- **Low Impact/High Effort**: Generally defer or eliminate

### **3. Implementation Planning**
Structure actions for real-world execution:

#### **Action Area Specification**
```yaml
action_id: ACT-001
finding_source: F-001
title: "Establish API Resilience Strategy"
description: "Develop approach for handling API failures and service interruptions"
category: technical_architecture
priority: critical
complexity: moderate
affected_components: ["payment_service", "external_apis"]
dependencies: ["service_discovery_strategy"]
success_concept: "System gracefully handles external service failures"
architectural_impact: "Improves operational resilience across service boundaries"
```

---

## 📝 Action Extraction Outputs

### **Action Area Summary**
Primary output organized by priority and theme:

```yaml
critical_actions:
  - action_id: ACT-001
    title: "Establish API Resilience Strategy"
    category: technical_architecture
    complexity: moderate
    affected_areas: ["service_integration", "error_handling"]
    
important_actions:
  - action_id: ACT-002
    title: "Define Data Consistency Approach"
    category: technical_architecture  
    complexity: moderate
    affected_areas: ["data_management", "service_boundaries"]

beneficial_actions:
  - action_id: ACT-003
    title: "Establish Monitoring Strategy"
    category: operational
    complexity: simple
    affected_areas: ["observability", "system_health"]
```

### **Implementation Themes**
```yaml
technical_architecture:
  focus_areas: ["service_resilience", "data_consistency", "integration_patterns"]
  complexity_assessment: "moderate to high"
  
operational_readiness:
  focus_areas: ["monitoring", "deployment", "incident_response"]
  complexity_assessment: "simple to moderate"
  
organizational_alignment:
  focus_areas: ["team_structure", "decision_processes", "skill_development"]
  complexity_assessment: "varies"
```

### **Logical Sequencing**
```markdown
## Foundation Phase
- Establish core architectural patterns
- Define service boundaries and integration approaches
- Set up basic operational capabilities

## Development Phase  
- Implement resilience and reliability patterns
- Develop data management strategies
- Enhance operational monitoring

## Evolution Phase
- Optimize based on operational experience
- Address advanced architectural concerns
- Scale organizational capabilities
```

### **Areas Requiring Stakeholder Input**
```yaml
architectural_decisions:
  - title: "Service decomposition strategy"
    description: "How granular should service boundaries be?"
    impact: "Affects development complexity and operational overhead"
    
  - title: "Data consistency approach"
    description: "Strong vs eventual consistency trade-offs"
    impact: "Influences system design and business logic"
    
technical_constraints:
  - title: "Technology stack selection"
    description: "Platform, frameworks, and tooling choices"
    impact: "Determines implementation approach and team skills needed"
    
business_priorities:
  - title: "Performance vs complexity trade-offs"
    description: "Acceptable complexity for performance gains"
    impact: "Guides architectural pattern selection"
```

---

## 🔄 Transition to Phase 9

**Hand-off to Final Report Generation:**
- Structured action list ready for inclusion in Action Plan template
- Resource requirements for Executive Summary budget discussions
- Implementation roadmap for stakeholder timeline planning
- Unresolved items for tracking and follow-up

---

## 💡 Example Action Extraction

```
Input Finding: "F-001: API resilience gaps threaten payment reliability - High Priority"

Extracted Action Area:
ACT-001: Establish Service Resilience Strategy
- Category: Technical Architecture
- Complexity: Moderate
- Affected Components: Payment Service, External API Integrations
- Dependencies: Service boundary definitions
- Success Concept: System handles external service failures gracefully
- Implementation Themes:
  * Error handling and retry patterns
  * Circuit breaker implementation
  * Monitoring and alerting for service health
  * Fallback mechanisms for critical paths
```

---

## ⚠️ Critical Guidelines

### **Conceptual Focus**
- **Every finding becomes action areas** - no conclusions without direction
- **Action areas guide detailed planning** - provide focus for subsequent design work
- **Complexity assessments are realistic** - based on architectural understanding
- **Dependencies are conceptually clear** - logical sequencing identified

### **Planning Integration**
- **Action areas inform design phases** - compatible with iterative architecture development
- **Priorities align with business goals** - reflects validated stakeholder input  
- **Themes support resource planning** - logical grouping for team allocation
- **Success concepts are achievable** - architectural outcomes are feasible

This phase ensures that architectural insights translate directly into project execution and business value delivery.