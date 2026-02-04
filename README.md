# Value-in-Motion™: The Agentic CS Operating System

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)]() [![Platform](https://img.shields.io/badge/platform-n8n%20%7C%20Claude-blue)]() [![License](https://img.shields.io/badge/license-Proprietary-orange)]()

**Value-in-Motion™** is an event-driven, AI-augmented architecture that transforms Customer Success from a reactive support function into a scalable revenue engine. It operationalizes the "Agentic CS" model to automate **80% of administrative overhead** while driving Net Revenue Retention (NRR).

---

## 🧠 The Core Logic: Engineering Revenue

Traditional Health Scores are lagging indicators. This framework treats Customer Success as an engineering problem, applying **Lean Manufacturing Principles** to SaaS telemetry data to detect risks before they appear on a dashboard.

| Lean Principle | In SaaS Terms | The Agentic Response |
| :--- | :--- | :--- |
| **Muda (Waste)** | Paying for unused licenses or features. | **Auto-Audit:** Agent identifies shelfware and drafts a "License Optimization Plan" to save the renewal. |
| **Mura (Inconsistency)** | Erratic login patterns or "spiky" adoption. | **Auto-Nudge:** Agent detects usage gaps and triggers targeted training workflows. |
| **Muri (Overburden)** | High volume of support tickets/complaints. | **Auto-Escalate:** Agent correlates ticket spikes with renewal dates and alerts the Director of CS. |

---

## 🏗️ System Architecture

This diagram represents the "Source Code" of the Agentic CS lifecycle—moving from manual touchpoints to autonomous loops.

```mermaid
flowchart TB
  %% INTELLIGENCE LAYER
  subgraph INTEL["🧠 AI Intelligence Layer (Claude 4.5)"]
    direction LR
    ai_engine["Orchestration Engine (n8n)"] --> ai_signals["Predictive Signals"]
    ai_engine --> ai_triggers["Event Triggers"]
  end
  
  %% AUTOMATED PHASES
  subgraph AUTO["⚡ Autonomous Execution"]
    direction TB
    a1["🤖 Data Ingestion (Usage/CRM)"] --> a2["🤖 Lean Analysis (Muda/Mura/Muri)"]
    a2 --> a3{Decision Gate}
    
    a3 -- Risk Detected --> a4["Trigger: Prevention Playbook"]
    a3 -- Opportunity --> a5["Trigger: Expansion Proposal"]
    a3 -- Routine --> a6["Trigger: Auto-QBR Generation"]
  end

  %% HUMAN LAYER
  subgraph HUMAN["👤 Strategic Intervention"]
    h1["Executive Relationship Strategy"]
    h2["Complex Negotiations"]
  end
  
  INTEL -.-> AUTO
  AUTO --> HUMAN
  HUMAN -.-> INTEL
```


## Value-in-Motion-agent
An agentic Customer Success auditor that identifies Lean waste (Muda, Mura, Muri) and automates strategic account health reviews
Value in Motion™: Agentic CS Audit Framework
This repository demonstrates the codification of my proprietary Customer Success methodology into an automated, AI-driven diagnostic engine.

The Core Problem
Traditional CS health scores are often static and reactive. This framework applies Lean principles (Muda, Mura, Muri) to telemetry data to identify hidden churn risks and expansion opportunities before they hit the dashboard.

Technical Execution
Workflow Engine: n8n (visual orchestrator).

Intelligence Layer: Claude 4.5 Sonnet (using a custom System Prompt grounded in CS logic).

Integrations: Google Sheets (Data Source) and Gmail (Automated Reporting).

Logic Blueprint
```mermaid
graph TD
    A[Start: Customer Data Input] --> B{Analyze Usage Patterns}

    B -->|Low Active Users| C["Detect: Muda (Waste)"]
    B -->|Erratic Logins| D["Detect: Mura (Inconsistency)"]
    B -->|High Ticket Volume| E["Detect: Muri (Overburden)"]

    C --> F[Action: License Optimization Plan]
    D --> G[Action: Adoption Training Plan]
    E --> H[Action: QBR & Support Alignment]

    F1 --> I["Output: 'Value in Motion' Workflows"]
    G1 --> I
    H1 --> I
```
## Real-World Impact
The agent successfully identified 75% Unused Capacity (Muda) and calculated an estimated $45,000/year in waste, providing an immediate strategic pivot for the CSM.

## Customer Success Management Activities
![Customer Success Lifecycle](CSM%20Activities%20Details.png)

## Claude Agentic Customer Success Operations — AI-Augmented Lifecycle
https://github.com/ValueInMotion/value-in-motion-agent/blob/main/agentic_cs_workflow.mmd
<iframe src="https://claude.site/public/artifacts/6327c6cb-62f8-4b6c-a007-3dd07bbd6681/embed" title="Claude Artifact" width="100%" height="600" frameborder="0" allow="clipboard-write" allowfullscreen></iframe>

## Agentic Customer Success Operations — Mermaid Flowchart
```mermaid
flowchart LR

CI[Central Intelligence Layer]

P1[Phase 1 - Automated Transition]
P2[Phase 2 - Intelligent Discovery]
P3[Phase 3 - AI Assisted Planning]
P4[Phase 4 - Autonomous Activation]
P8[Phase 8 - Automated Value Proof]
P10[Phase 10 - Relationship Intelligence]
P11[Phase 11 - Intelligent Churn Response]

L1((Autonomous Orchestration))
L2((Real-Time Observability))
L3((Proactive Risk Management))

EXP[AI-Driven Expansion Engine]

CI --> P1
P1 --> P2
P2 --> P3
P3 --> P4
P4 --> P8
P8 --> P10
P10 --> P11

CI --- L1
CI --- L2
CI --- L3

P8 --> EXP
EXP --> P10
```

