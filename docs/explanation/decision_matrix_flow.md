---
title: "Decision Matrix Workflows (Visual)"
tags: ["sales", "workflow", "decision-matrix", "mermaid", "explanation"]
created_at: "2026-08-10"
last_updated_at: "2026-08-10"
---

# Decision Matrix Workflows

This document visualizes the evaluation pipeline for consulting prospects. It serves as the blueprint for the programmatic JSON decision matrix.

## 1. Primary Qualification Pipeline (The "Kill Switch")

This flowchart demonstrates the immediate binary filters applied to any new lead.

```mermaid
graph TD
    A[New Prospect Identified] --> B{Involves HIPAA/PCI/Sensitive Data?}
    B -- Yes --> Z[DISQUALIFY: High Liability]
    B -- No --> C{Speaking to Final Decision Maker?}
    C -- No --> Y[DISQUALIFY: Gatekeeper Block]
    C -- Yes --> D{Is this their Core Customer Product?}
    D -- Yes --> X[DISQUALIFY: High Risk/24-7 Liability]
    D -- No --> E{Is the Definition of Done clear & binary?}
    E -- No --> W[DISQUALIFY: Scope Creep Risk]
    E -- Yes --> F[PASS: Proceed to Service Alignment]
```

## 2. Service Alignment & Categorization

Once a prospect passes the kill switch, their primary pain point determines the service alignment.

```mermaid
graph TD
    F[Qualified Prospect] --> G{Primary Pain Point?}
    
    G -- Fragmented Data / Manual Reporting --> H[Backend & Data Engineering]
    G -- Manual Deployments / Server Instability --> I[DevOps & Infrastructure]
    G -- Unstructured Data / Manual Triage --> J[Advanced Automation & AI]
    
    H --> K[Propose: ETL Pipeline or Integration]
    I --> L[Propose: CI/CD setup or IaC Migration]
    J --> M[Propose: Semantic Parsing or Agent Workflow]
```

## 3. Financial Viability & Proposal

The final check before drafting a proposal ensures the project meets the minimum financial floor.

```mermaid
graph TD
    N[Service Aligned] --> O{Estimated Project Complexity}
    
    O -- Low (Scripts, Simple CI/CD) --> P{Client Budget >= $1,000?}
    O -- Medium (ETL, Custom Integrations) --> Q{Client Budget >= $1,500?}
    O -- High (Semantic AI, Complex Domains) --> R{Client Budget >= $2,000?}
    
    P -- No --> S[Reject or Downscope]
    Q -- No --> S
    R -- No --> S
    
    P -- Yes --> T[Draft Proposal: Flat Fee]
    Q -- Yes --> T
    R -- Yes --> T
    
    T --> U{Is ongoing maintenance required?}
    U -- Yes --> V[Add $500+/mo Retainer to Proposal]
    U -- No --> W[Finalize One-Off Proposal]
```
