---
title: "How to Evaluate a Prospect"
tags: ["sales", "process", "evaluation", "how-to"]
created_at: "2026-08-10"
last_updated_at: "2026-08-10"
---

# How to Evaluate a Prospect

This guide outlines the standard operating procedure (SOP) for running a new prospect through the decision matrix.

## Step 1: Lead Capture
When a new prospect is identified, create a JSON file in `data/prospects/` (e.g., `acme_corp.json`) containing basic information: URL, industry, contact title, and the perceived technical pain point.

## Step 2: Apply Disqualifiers (The Kill Switch)
Cross-reference the prospect's request against the `docs/reference/targeting_filters.md`.
1. Does the project involve HIPAA or PCI data?
2. Is the contact someone other than a primary decision-maker?
3. Is this their core, customer-facing product?
4. Is the definition of "done" vague?

*If YES to any of the above, disqualify the lead immediately. Do not proceed to Step 3.*

## Step 3: Matrix Scoring
Evaluate the prospect against the `data/decision_matrix.json` (via agent logic or manual review).
1. **Determine Category Fit:** Does their pain point align with Backend/Data, DevOps, or AI?
2. **Determine Budget Viability:** Based on the `docs/reference/service_catalog.md`, can their problem be solved profitably at or above the $1,000 floor?

## Step 4: Proposal Generation
If the prospect passes the evaluation, draft a targeted pitch.
1. Reference their specific manual process or bottleneck.
2. Propose the relevant service from the catalog.
3. State the binary outcome (the Definition of Done).
4. Provide the minimum flat-fee or retainer cost.
