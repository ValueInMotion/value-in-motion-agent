# I. Value-in-Motion™ — Agentic AI Lifecycle Orchestration Engine
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)]() 
[![Platform](https://img.shields.io/badge/platform-Python%20%7C%20Claude-blue)]() 
[![Framework](https://img.shields.io/badge/framework-LangChain-black)]() 
[![Orchestration](https://img.shields.io/badge/orchestration-LangGraph-purple)]() 
[![Observability](https://img.shields.io/badge/observability-LangSmith-orange)]() 
[![License](https://img.shields.io/badge/license-Proprietary-orange)]()

---

## 1. What It Is

**Value in Motion is an agentic execution operating system for Customer Success. Adoption creates evidence, evidence validates outcomes, outcomes drive value — and value drives the decision to remediate, renew, or expand. Forty-four governed steps, handoff through renewal and expansion.**

**ViM (Value in Motion)** is a closed-loop agentic execution process that turns an outcome goal into actions, learns from results, and keeps iterating until value is delivered.

- **Get the Mission (Objective Function):** This prevents the agent from hallucinating or drifting. By defining "what success looks like" upfront, the agent has a definitive metric to measure its progress against during the final iteration step.
- **Scan the Scene (Context & RAG):** Agents are only as good as their situational awareness. This step effectively combines memory retrieval, real-time data ingestion, and constraint checking, ensuring the agent doesn't act blindly.
- **Think It Through (Planning & Reasoning):** This acts as the Chain-of-Thought (CoT) phase. Breaking a large mission into subgoals and identifying the necessary tool calls prevents the agent from attempting to solve complex problems in a single, error-prone leap.
- **Take Action (Tool Use / Function Calling):** This is where the model connects to the real world. By limiting execution to one concrete step at a time, you minimize the blast radius of potential errors.

Value in Motion™ detects **value friction**, anticipates **risk from day one**, and **orchestrates targeted actions** across the entire customer lifecycle.

It operates in closed loops:

**Detect → Diagnose → Decide → Act → Observe → Improve**

> Not a dashboard.  
> Not a chatbot.  
> A lifecycle decision and execution engine. 

---

## Operating Model

An operating model in which every Customer Success action is executed as a **governed agentic work unit**, producing evidence as a by-product, so that customer value is continuously measured and every executive decision is made against **proof rather than opinion**.

**4 lifecycle stages · 11 phases · 44 governed execution steps · 6 agentic layers**

### 1 · Unit of Work — the Agentic Work Unit (AWU)

Every execution step is an AWU with four required attributes:

| Attribute | Definition |
|---|---|
| **Trigger** | The signal or event that initiates the unit |
| **Action** | The permitted operation, scoped and bounded |
| **Owner** | Human, agent, or human-in-the-loop pairing |
| **Evidence** | The artifact the unit must emit on completion |

Nothing runs undefined. Nothing runs without leaving a trace.

### 2 · Control Plane — Permission Tiers

Each AWU is classified into one of three tiers:

- **`AUTO`** — executes without human intervention
- **`APPROVAL-REQUIRED`** — executes on human gate
- **`BLOCKED`** — policy-denied, logged, escalated

**The tier mix is itself a health metric.** Rising `APPROVAL-REQUIRED` indicates trust not yet earned. Rising `BLOCKED` indicates policy misaligned with the work.

### 3 · Evidence Layer — Adoption Becomes Signal

Observability across all 11 phases. Adoption telemetry, risk signals, and outcome attainment are captured as **traces**, not assembled manually at QBR time.

**Primary measure: time-to-audit-evidence** — how fast an outcome can be proven when an executive asks.

### 4 · Decision Layer — the Closing Loop

Measured value routes to one of three executive decisions: **remediate**, **renew**, or **expand**.

The loop is what makes this an operating model rather than a lifecycle diagram: **the output of measurement is a mandated decision, not a report.**

---

## Lifecycle — 4 Stages, 11 Phases

### 1. **Handoff** — 2 phases
- Internal Transition
- Predictable Success Profile

### 2. **Onboarding** — 2 phases
- Customer Kickoff
- Value Activation

### 3. **Value Realization** — 6 phases
- Strategic Orchestration
- Observability & Signals
- Risk Control
- Churn Handling
- Advocacy
- Value Proof

### 4. **Renewal & Expansion** — 1 phase
- Renewal & Expansion

---

## The Loop

```mermaid
flowchart LR
    A[**Handoff**<br/>context transfers<br/>with intent intact] --> B[**Onboarding**<br/>activation produces<br/>first evidence]
    B --> C[**Value Realization**<br/>orchestrate · observe<br/>control · prove]
    C --> D[**Renewal & Expansion**<br/>remediate · renew · expand]
    D -->|decision becomes<br/>new baseline| A
```

---

## Framework vs. Operating Model

| Framework | **Value in Motion** |
|---|---|
| Describes phases | **Defines execution units** |
| Assigns owners | **Assigns permission tiers** |
| Reports on health | **Emits evidence continuously** |
| Recommends action | **Forces a decision** |
| Reviewed quarterly | **Runs continuously** |

---

## In One Line

> **It is not a lifecycle map. It is an execution model where the work is governed, the evidence is a by-product of doing the work, and the measurement forces a decision.**

---

## The Agentic Stack
**`6 Domains · 21 Layers`**

<img width="1472" height="1560" alt="image" src="https://github.com/user-attachments/assets/de125e0b-ba7c-45d6-b5ae-5b2848b61f53" />


----
## 2. Why It Matters

Customer Success does not fail due to a lack of data.
It fails due to a lack of structured execution.

Most CS teams:
- Track health scores
- React to churn signals
- Coordinate manually across tools

Value in Motion™ transforms Customer Success from reactive tracking to **proactive revenue orchestration**.

---

## 3. Who It Is For

- **Customer Success Leaders (CSM / CS Ops)** scaling retention and operational rigor
- **Series A–C SaaS Founders** building predictable revenue engines
- **Revenue & GTM teams** focused on NRR and expansion
- **AI / Agentic builders** designing autonomous SaaS workflows

---

## 4. Expected Impact

- **-+20–40% Net Revenue Retention uplift**
- **–30% manual CSM workload**
- **30–90 days earlier renewal risk detection**
- **Stronger expansion signal visibility**
- **Structured lifecycle governance**

---

## 5. Current Scope (What works today)

- ✅ Risk Detection Agent (Sales → Adoption → Renewal)
- ✅ Lifecycle-based phase scoring logic
- ✅ Phase-level diagnostic output (identify broken stage)
- ✅ Actionable recommendations
- ✅ Local execution engine (Python)

**In Progress** 

- ⏳ Multi-agent lifecycle orchestration (LangGraph full loop)
- ⏳ CRM + telemetry integration
- ⏳ LLM-powered reasoning layer
- ⏳ Autonomous execution tools (email, CRM updates, alerts)

---

## 6. Strategic Positioning

Value in Motion™ is not a chatbot.
It is a **Revenue Operating System** ensuring value flows continuously from:

**Intent → Outcomes → Adoption → Impact → ROI → Expansion → Reinvestment → Renewal**

When value flows, revenue follows.

---

## 7. Live Demo — risk_detection_agent (V0)

A runnable lifecycle-aware agent detecting churn risk across:

**Sales → Adoption → Renewal**

Run locally:
pip install -r requirements.txt
python -m src.risk_agent.main

**System Flow — Risk Detection Agent**

![My Image](docs/diagrams/risk_agent.png)

**#1. INPUTS — Signals Enter the System**

Source
- `examples/sample_account.json`
- (future: CRM, telemetry, product usage)

Signals
- ICP fit
- Usage metrics
- Stakeholders
- Deal complexity
- ROI signals

&rarr; Raw customer reality.


**#2. VALIDATION — Structured Input**

File: `schemas.py`

- Pydantic validation
- Data standardization
- Garbage-in protection

&rarr; Turns signals into a trusted state.


**#3. DECISION ENGINE — Lifecycle Diagnosis**

File: `agent.py`

- Risk scoring (LOW / MEDIUM / HIGH)
- Root cause detection
- Phase break mapping
- Recommended corrective motion

&rarr; This is the deterministic lifecycle brain &rarr;  probabilistic AI


**#4. ORCHESTRATION — Execution Runtime**

**File:** `main.py`

- Load signals
- Invoke agent
- Output structured decision

&rarr; Orcchestrate Value-in-Motion™ framework


**#5. OUTPUT — Decision-Ready Insight**

=== VALUE IN MOTION — RISK AGENT ===

Account: ACME
Risk: HIGH
Reasons: Low ICP fit, High deal complexity, Low usage (30d), No workflow integration, No executive engagement
Action: Recovery: exec alignment + value proof plan (14 days)

&rarr; Not analytics.  
&rarr; Actionable motion. 
 
---

## 8. Core Architecture

```mermaid
flowchart TB
  A[Signals] --> B[Validation Layer]
  B --> C[Lifecycle Diagnosis Engine]
  C --> D[Phase Break Detection]
  D --> E[Corrective Motion Recommendation]
  E --> F[Execution Layer]
  F --> G[Observation Loop]
  G --> C
  ```

## 9. Lifecycle Model

The agent operates against a strict lifecycle state machine:

**Intent → Outcomes → Workflow → Operational Change → Adoption → Usage → Impact → Value → Expansion → Executive Validation → Reinvestment**

Risk = friction in one of these phases.

> High Risk ≠ churn prediction.  
> High Risk = broken value flow.

---

## 10. Lean Philosophy — Zero Waste CS

> Applying Lean (Muda, Mura, Muri) to SaaS telemetry:  

| Lean Concept         | SaaS Reality      | Agent Response               |
| -------------------- | ----------------- | ---------------------------- |
| Muda (Waste)         | Shelfware         | License optimization plan    |
| Mura (Inconsistency) | Adoption gaps     | Targeted enablement workflow |
| Muri (Overload)      | Escalation spikes | Pre-renewal mitigation       |

> The agent scans continuously for structural inefficiency before revenue impact.  

---

## 11. Technical Stack (MVP)

- **Orchestration:** LangGraph
- **LLM Layer:** Claude / GPT
- **Framework:** LangChain
- **Observability:** LangSmith
- **Telemetry:** Pandas / SQL
- **Execution Layer:** Python runtime

Structured for:  
- Unit testing
- Integration testing
- Eval-driven development
- CI/CD readiness

---

## 12. What Makes It Different

Most automation:
- Linear workflows
- Static triggers
- Human-dependent orchestration

Value-in-Motion™:
- Stateful lifecycle reasoning
- Persistent account memory
- Gated phase transitions
- Loop resolution until criteria met
- Human-in-the-loop governance

Human = Supervisor
Agent = Lifecycle Executor

---

## 13. MVP Success Criteria

- ≥30% time saved per CSM
- Renewal brief auto-generated with ≥80% relevance
- Expansion surfaced before the renewal window
- Lean waste auto-detected
- No dropped stakeholder

---

## 14. Vision

Customer Success today:
- Reactive
- Fragmented
- Signal-blind

Value-in-Motion™:
- Structured
- Stateful
- Signal-driven
- Autonomous
- Expansion-oriented

From relationship management  
→ To autonomous revenue orchestration.

---

## 15. Positioning

Value-in-Motion™ is not:
- a CRM
- a dashboard
- a reporting tool

It is:

→  An Autonomous Customer Success Operating System

---


# II. Value-in-Motion™Architecture

## 1. Autonomous Agentic Layer

**#1. Action Library Layer**

- 4 Stages:  
**→ Hands-off → Onboarding → Value Realization → Renewal/Expansion**
  
- 11 Phases:  
**→ Transition → Kickoff → Workflow Integration → Orchestration → Observatory → Risk Mitigation  → Churn → Value ROI → Renewal/Upsell → Advocacy → VoC**
    
- 44 Steps:  
**→ Action Library**


**#2. Policy Governance Layer**

- AUTO (can run alone)
- APPROVAL REQUIRED (CSM must approve)
- BLOCKED (never allowed)

**#3. Autonomous Layer**

- **Autonomous = Planner × State × Loop × Tools × Policy**  
  
- **Planner:** Reasoning Engine
- **State:** Memory + Context
- **Orchestration (Loop):** Detect → Decide → Act → Observe → Update → Repeat
- **Tools:** CRM (Salesforce), Telemetry (Quicksign), UX behavior (Pendo), CS SaaS (Planhat), MCP, API, DB...
  
---

## 2. Tech Stack (MVP)

- **Orchestration**: LangGraph (Python)
- **LLM**: Claude 3.5 Sonnet / GPT-4o
- **Framework**: LangChain
- **Observability**: LangSmith
- **Data Sources**: Salesforce / Planhat / Snowflake / LlamaIndex
- **Telemetry Analysis**: Pandas / SQL
  
![Value in Motion CSM Autonomous Agent](docs/diagrams/Value%20in%20Motion%E2%84%A2%20CSM%20Autonomous%20Agent.png)


**Stateful Orchestration**

This system moves beyond simple "Trigger -> Action" automation. It uses LangGraph to implement a State Machine. The agent has a "Long-Term Memory" (State) for each account and persists context across days or weeks.

```mermaid
flowchart TB
    subgraph Memory ["💾 Persistence Layer (Checkpointers)"]
        State["Account State<br/>(Phase, Risk Score, Missing Fields)"]
    end

    Start((Start)) --> Router{Phase Router}

    %% PHASE 1: TRANSITION
    Router -->|Phase 1| P1[Node: Handoff Audit]
    P1 --> G1{Gate: Data Ready?}
    G1 -- No --> L1[Loop: Fetch Missing Anchors]
    L1 --> P1
    G1 -- Yes --> P1_Exit[Update State: Ready for Phase 2]

    %% PHASE 2: DIAGNOSTIC
    P1_Exit --> P2[Node: Diagnostic Agent]
    P2 --> Q1[Task: Stakeholder Mapping]
    P2 --> Q2[Task: Pain Metric Check]
    Q1 & Q2 --> Risk{Risk Detected?}
    
    Risk -- Yes --> Escalate[Node: Draft Risk Mitigation Plan]
    Risk -- No --> CSP[Node: Draft Success Plan]

    %% PHASE 4: VELOCITY
    CSP --> P4[Node: Velocity Sensors]
    P4 --> S1[Check: TTV Metrics]
    P4 --> S2[Check: License Utilization]
    
    S1 & S2 --> NBA[Node: Next Best Action Queue]
    
    %% HUMAN INTERVENTION
    Escalate -.-> Human((👤 Human Approval))
    Human -->|Approve| Action[Execute Mitigation]
    Human -->|Reject| Replan[Re-Reason Strategy]
```

---

## 3. Repository Structure

```css
value-in-motion-agent/
├── src/
│   ├── graph/
│   │   ├── __init__.py
│   │   ├── state.py           # Defines the AccountState (TypedDict)
│   │   ├── nodes.py           # Core logic (Audit Node, Diagnostic Node)
│   │   ├── edges.py           # Conditional logic (Gates and Routers)
│   │   └── compiled_graph.py  # The LangGraph entry point
│   ├── tools/
│   │   ├── crm_tools.py       # Salesforce/HubSpot connectors
│   │   ├── email_tools.py     # Draft generation
│   │   └── data_tools.py      # Telemetry analysis (Pandas/SQL)
│   └── prompts/
│       ├── auditor_prompt.yaml
│       └── strategist_prompt.yaml
├── tests/
│   ├── unit/                  # Function tests
│   └── integration/           # Full graph run tests
├── docs/
│   ├── architecture.mmd
│   └── setup_guide.md
├── requirements.txt
└── .env.example
```

Structured for:
- Unit testing
- Integration testing
- Eval-driven development
- CI/CD compatibility


## 4. Use Case: risk-agent Repository Flow Chart

```mermaid
flowchart TB
  R[value-in-motion-agent/]

  R --> SRC[src/]
  R --> EX[examples/]
  R --> DOC[docs/]
  R --> REQ[requirements.txt]
  R --> RD[README.md]

  SRC --> RA[src/risk_agent/]
  RA --> MAIN[main.py]
  RA --> AG[agent.py]
  RA --> SC[schemas.py]
  RA --> DATA[data/]
  DATA --> ACC[accounts.json]

  EX --> OUT[risk_agent_output.txt]

  RD -->|links to| OUT
  RD -->|shows diagram| DOC
```

---

## 5. Observability & Evals

The agent is treated as production software.

**Core Metrics**
1. Handoff audit accuracy
2. False-positive risk detection
3. Draft safety compliance
4. Token cost per account
5. Time saved per lifecycle phase

Every execution is traceable and regression-tested in LangSmith.

---

## 6. Installation

```bash
git clone https://github.com/ValueInMotion/value-in-motion-agent.git
cd value-in-motion-agent
pip install -r requirements.txt
cp .env.example .env
```

---
