# value-in-motion-agent
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

