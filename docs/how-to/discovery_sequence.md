---
title: "Systematized Discovery Sequence"
tags: ["sales", "prospecting", "workflow", "how-to"]
created_at: "2026-08-10"
last_updated_at: "2026-08-10"
---

# Systematized Discovery Sequence

This guide details the step-by-step process for investigating a local company (Kalamazoo/Portage area) and determining which consulting product bucket they require, minimizing time wasted on unqualified leads.

## Phase 1: Digital Reconnaissance (Passive Investigation)
Before ever contacting the prospect, you must gather passive intelligence to identify symptoms of inefficiency.

1.  **Analyze Job Postings:** Look at their "Careers" page or LinkedIn job listings. 
    *   *Signal:* Hiring for "Data Entry," "Operations Coordinator," or "Admin Assistant" often indicates they are throwing cheap human labor at a problem that should be solved with a data pipeline (ETL).
2.  **Inspect the Public Tech Stack:** Use browser extensions like Wappalyzer or BuiltWith on their domain.
    *   *Signal:* Outdated frameworks, multiple disjointed subdomains, or slow load times indicate a need for DevOps/Infrastructure modernization.
3.  **Review Employee Roster:** Search LinkedIn for their team structure.
    *   *Signal:* If they have a large team of "Analysts" but no "Data Engineers," they are likely doing reporting manually in Excel.

## Phase 2: The "Trojan Horse" Audit (Active Outreach)
Do not pitch generic services (e.g., "I build software"). Pitch a hyper-specific observation uncovered during Phase 1 to secure a conversation.

1.  **Craft the Observation:** Tie your tech stack findings to a business pain point.
    *   *Example:* "I noticed your logistics agency uses three different client portals, but you are also hiring for manual data entry clerks. I build local systems that sync these portals automatically."
2.  **Offer the Free Audit:** Ask for 15 minutes to review their technical bottleneck, framing it as an educational conversation rather than a hard sales pitch.

## Phase 3: The Discovery Call (The Interrogation)
The goal of this call is not to sell immediately, but to execute the [Symptom Tests](../reference/symptom_tests.md) and bucket the client.

1.  **Avoid Technical Jargon:** Do not ask about their databases or servers. Business owners care about time, money, and risk.
2.  **Ask the Golden Question:** 
    *   *"What is the most manual, annoying, or error-prone task your team has to do every Friday afternoon?"*
3.  **Listen for the Buckets:**
    *   If they complain about copying data -> **Backend & Data Engineering**.
    *   If they complain about system crashes or manual updates -> **DevOps & Infrastructure**.
    *   If they complain about drowning in paperwork/emails -> **Advanced Automation & AI**.
4.  **Confirm the Definition of Done:** Before ending the call, ensure their problem can be solved with a binary outcome (e.g., "If I can make system A talk to system B automatically by next month, would that solve this bottleneck?").

## Phase 4: Matrix Scoring & Proposal
Following the call, run the gathered intelligence through the decision matrix outlined in the [Evaluate Prospect Guide](evaluate_prospect.md) to generate a flat-fee proposal.
