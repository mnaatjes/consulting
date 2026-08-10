---
title: "Agent Business Rules"
tags: ["agents", "rules", "system", "reference"]
created_at: "2026-08-10"
last_updated_at: "2026-08-10"
---

# Agent Business Rules

These rules dictate how AI agents must behave when evaluating leads, generating proposals, or assisting with consulting business operations.

## 1. Strict Filter Adherence
Agents must automatically disqualify any prospect that triggers a "Kill Criteria" listed in `docs/reference/targeting_filters.md`. Under no circumstances should an agent recommend pursuing a project involving HIPAA/PCI compliance, non-decision makers, or core product development.

## 2. Floor Pricing Enforcement
Agents must reference `docs/reference/service_catalog.md` when drafting proposals. No proposal should ever be generated with a suggested value lower than $1,000 for a project or $500/month for a retainer. 

## 3. Scope Containment
When drafting technical scopes of work, agents must ensure the Definition of Done is binary and measurable. Agents must rewrite vague client requests (e.g., "Make it better") into explicit technical deliverables (e.g., "Automate JSON extraction via cron job").

## 4. Prioritize Process over Product
If a client request straddles the line between internal process and core product, the agent must advise the consultant to steer the conversation strictly toward the internal process components.

## 5. Concise Output
When outputting prospect evaluations, agents must provide a direct "Go/No-Go" decision upfront, followed by a bulleted justification mapping to the decision matrix. Conversational filler is strictly prohibited.
