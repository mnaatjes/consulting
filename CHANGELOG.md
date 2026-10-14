# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased] - 2026-08-10

### Added
- **Automated Audit System:** 
  - Created `scripts/project_auditor.py` to extract dependencies, architecture signatures, and infrastructure metadata from local/remote git repositories.
  - Generated JSON audits for 9 historical projects in the `data/` directory.
  - Created `scripts/update_audits.py` to embed AI-generated consulting capabilities and business value mappings into the JSON audits.
- **Consulting Strategy Definition:**
  - Defined the three core consulting buckets: Backend Architecture & Data Engineering, DevOps & Infrastructure, and Advanced Automation & AI Integration.
  - Documented the capability audit and consulting niche definitions in `docs/explanation/capability_audit_summary.md`.
- **Prospecting & Sales Framework:**
  - Established binary kill criteria and target filters in `docs/reference/targeting_filters.md`.
  - Defined minimum pricing floors and service offerings in `docs/reference/service_catalog.md`.
  - Created standard operating procedures for prospect evaluation (`docs/how-to/evaluate_prospect.md`) and systematized discovery sequences (`docs/how-to/discovery_sequence.md`).
  - Documented symptom-based product alignment tests in `docs/reference/symptom_tests.md`.
  - Enforced AI operational constraints via `docs/reference/agent_business_rules.md`.
- **Legal & Business Infrastructure:**
  - Provided step-by-step guides for LLC formation (`docs/how-to/form_michigan_llc.md`) and acquiring business insurance (`docs/how-to/obtain_business_insurance.md`).
  - Documented legal contract hierarchies (MSA/SOW/NDA) in `docs/reference/master_services_agreement.md` and `docs/reference/auxiliary_legal_documents.md`.
  - Created a prioritized, zero-cost-first infrastructure shopping list (`docs/reference/business_infrastructure_inventory.md`).
- **Workflow Visualization:**
  - Built comprehensive Mermaid flowcharts mapping the decision matrix from lead capture to legal execution (`docs/explanation/decision_matrix_flow.md`).
  - Mapped the 4 holistic Master Business Pipelines (Foundation, Sales, Delivery, Administration) with hierarchy trees in `docs/explanation/master_business_pipelines.md`.

### Context
* **Conversation ID:** [0cf1c18c-876e-46f7-90bf-63c951ac0307](conversation://0cf1c18c-876e-46f7-90bf-63c951ac0307)
