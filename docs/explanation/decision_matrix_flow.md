---
title: "Decision Matrix Workflows (Visual)"
tags: ["sales", "workflow", "decision-matrix", "mermaid", "explanation"]
created_at: "2026-08-10"
last_updated_at: "2026-08-10"
---

# Decision Matrix Workflows

This document visualizes the evaluation pipeline for consulting prospects. It serves as the blueprint for the programmatic JSON decision matrix, from initial discovery to final proposal, and through legal onboarding.

## 1. Systematized Discovery Sequence

This flowchart demonstrates the passive and active intelligence gathering phases before a formal evaluation begins.

```mermaid
graph TD
    A[Identify Local Prospect] --> B[Phase 1: Digital Reconnaissance]
    B --> C{Analyze Job Postings}
    B --> D{Inspect Public Tech Stack}
    C --> |Hiring Data Entry / Admins| E[Flag for Data Engineering]
    D --> |Outdated / Brittle Stack| F[Flag for DevOps]
    E --> G[Phase 2: Craft Trojan Horse Observation]
    F --> G
    G --> H[Offer Free 15-Minute Audit]
    H --> |Accepted| I[Phase 3: The Discovery Call]
    H --> |Rejected| J[Move to Next Prospect]
```

## 2. Symptom Testing Logic (The Discovery Call)

During the Discovery Call, technical jargon is avoided in favor of operational symptom testing.

```mermaid
graph TD
    I[Start Discovery Call] --> K[Ask the Golden Question:<br/>What is your most annoying Friday task?]
    K --> L{Client's Response Symptom}
    
    L --> |Copying data / spreadsheets| M[The 'Ctrl+C / Ctrl+V' Test]
    L --> |System crashes / deployment fear| N[The 'Server Fear' Test]
    L --> |Manual document reading / routing| O[The 'Reading Fatigue' Test]
    
    M --> P[Bucket: Backend & Data Engineering]
    N --> Q[Bucket: DevOps & Infrastructure]
    O --> R[Bucket: Advanced Automation & AI]
    
    P --> S[Confirm Binary Definition of Done]
    Q --> S
    R --> S
    S --> T[Proceed to Formal Qualification Matrix]
```

## 3. Primary Qualification Pipeline (The "Kill Switch")

This flowchart demonstrates the immediate binary filters applied to the prospect's request after the discovery call.

```mermaid
graph TD
    T[Initiate Matrix Scoring] --> U{Involves HIPAA/PCI/Sensitive Data?}
    U -- Yes --> Z[DISQUALIFY: High Liability]
    U -- No --> V{Speaking to Final Decision Maker?}
    V -- No --> Y[DISQUALIFY: Gatekeeper Block]
    V -- Yes --> W{Is this their Core Customer Product?}
    W -- Yes --> X[DISQUALIFY: High Risk/24-7 Liability]
    W -- No --> E2{Is the Definition of Done clear & binary?}
    E2 -- No --> W2[DISQUALIFY: Scope Creep Risk]
    E2 -- Yes --> F2[PASS: Proceed to Service Alignment]
```

## 4. Service Alignment & Categorization

Once a prospect passes the kill switch, the bucket identified in the Symptom Test dictates the service proposed.

```mermaid
graph TD
    F2[Qualified Prospect] --> G2{Bucket Identified in Discovery?}
    
    G2 -- Backend & Data Engineering --> K2[Propose: ETL Pipeline or Integration]
    G2 -- DevOps & Infrastructure --> L2[Propose: CI/CD setup or IaC Migration]
    G2 -- Advanced Automation & AI --> M2[Propose: Semantic Parsing or Agent Workflow]
```

## 5. Financial Viability & Proposal

The final check before drafting a proposal ensures the project meets the minimum financial floor.

```mermaid
graph TD
    N2[Service Aligned] --> O2{Estimated Project Complexity}
    
    O2 -- Low (Scripts, Simple CI/CD) --> P2{Client Budget >= $1,000?}
    O2 -- Medium (ETL, Custom Integrations) --> Q2{Client Budget >= $1,500?}
    O2 -- High (Semantic AI, Complex Domains) --> R2{Client Budget >= $2,000?}
    
    P2 -- No --> S2[Reject or Downscope]
    Q2 -- No --> S2
    R2 -- No --> S2
    
    P2 -- Yes --> T2[Draft Proposal: Flat Fee]
    Q2 -- Yes --> T2
    R2 -- Yes --> T2
    
    T2 --> U2{Is ongoing maintenance required?}
    U2 -- Yes --> V2[Add $500+/mo Retainer to Proposal]
    U2 -- No --> W3[Finalize One-Off Proposal]
```

## 6. Legal Execution & Onboarding Workflow

Once a client verbally accepts a proposal, this strict sequence dictates the legal paperwork execution before any technical work begins.

```mermaid
sequenceDiagram
    participant Consultant
    participant Client
    participant Accounting

    Note over Consultant, Client: Proposal Verbally Accepted
    
    alt Deep Technical Audit Required for SOW
        Consultant->>Client: Send Mutual NDA (MNDA)
        Client-->>Consultant: Sign MNDA
        Client-->>Consultant: Share Private Architecture/Data
    end
    
    Consultant->>Consultant: Draft Statement of Work (SOW)
    
    alt New Client (No existing MSA)
        Consultant->>Client: Send Master Services Agreement (MSA)
        Consultant->>Client: Send Statement of Work (SOW)
        Client-->>Consultant: Sign MSA & SOW
    else Existing Client
        Consultant->>Client: Send Statement of Work (SOW)
        Client-->>Consultant: Sign SOW
    end
    
    Consultant->>Accounting: Send W-9 Form & Initial Invoice (if applicable)
    Accounting-->>Consultant: Process Payment / Setup Vendor Profile
    
    Note over Consultant, Client: ONLY NOW: Commence Technical Work
```
