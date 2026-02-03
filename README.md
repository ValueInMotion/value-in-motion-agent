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
