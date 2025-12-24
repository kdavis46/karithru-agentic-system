# KarithruAI
 — Agentic Order Fulfillment System

KarithruAI is a deterministic, agentic execution system designed to carry operational workflows from input to outcome with human-in-the-loop governance.

This project demonstrates **spec-driven development**, deterministic decision logic, and enterprise-grade operational design principles rather than model-centric experimentation.

---

## Problem Statement

Manual hardware order processing introduces significant operational risk and inefficiency:

- Orders require multiple manual touchpoints across email, CRM, and inventory systems
- Human data entry leads to transcription errors and delayed fulfillment
- Fixed staffing capacity creates bottlenecks during demand spikes
- High labor costs reduce operational margins and customer satisfaction

KarithruAI addresses these issues by automating routine workflows while preserving human oversight for high-risk and non-standard cases.

---

## System Objectives

- **End-to-end processing time:** ≤ 5 minutes per order
- **Accuracy target:** ≥ 99.8%
- **Customer satisfaction:** ≥ 95%
- **Operational cost reduction:** ≥ 60% vs manual processing

---

## Architecture Overview

KarithruAI is implemented as a deterministic agent orchestrator with clear separation of concerns:


Input Processing → Decision Engine → Action Execution → Audit Logging


### Core Components

- **Input Processing**
  - Real-time email intake
  - PDF order extraction
  - Metadata normalization and validation

- **Decision Engine**
  - Customer validation via CRM (Salesforce stub)
  - Inventory availability checks
  - Order risk evaluation
  - Explicit YES / NO / ESCALATE outcomes

- **Action Layer**
  - Customer confirmations
  - Fulfillment notifications
  - Escalation handling

- **Audit & Monitoring**
  - Immutable event logs
  - Processing-time measurement
  - Decision traceability

---

## Governance & Autonomy Boundaries

### Autonomous Actions
- Order ingestion and parsing
- Routine validation checks
- Standard inventory-based fulfillment decisions
- Customer confirmation dispatch

### Human-Controlled Decisions
- Policy exceptions
- High-value orders
- Inventory shortages requiring sourcing decisions
- Ambiguous or anomalous orders

KarithruAI does **not** override policy, compliance, or irreversible actions without explicit human approval.

---

## Project Structure

KarithruAI/
├── app.py
├── models.py
├── decision_engine.py
├── exceptions.py
├── config.py
├── integrations/
│ ├── salesforce.py
│ ├── inventory.py
│ └── email_sender.py
├── monitoring/
│ └── audit.py
├── tests/
│ └── test_decision_engine.py
├── LICENSE
└── README.md



---

## Testing

The system includes deterministic unit tests covering:

- Successful order approval paths
- Invalid customer escalation
- Inventory unavailability handling
- High-value order escalation
- Anomalous order detection

Run tests locally:

```bash
pytest -v


Design Principles Demonstrated

Spec-driven development

Deterministic business logic

Clear auditability

Human-in-the-loop governance

Enterprise-ready structure

Test-first validation of decision paths

This project intentionally avoids premature complexity (async frameworks, external SDKs, ML models) in favor of clarity, correctness, and control.





License

This project is licensed under the Apache License 2.0.

Copyright © 2025 Zayis LLC
