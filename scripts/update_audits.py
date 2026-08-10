import json
from pathlib import Path

DATA_DIR = Path("data")

# AI-Generated insights mapped by project name
INSIGHTS = {
    "server-migration": {
        "key_capabilities_proven": ["Implemented Infrastructure as Code (IaC) and GitOps workflows", "Automated server configuration using Ansible", "Structured Active Directory and network topologies"],
        "business_value_mapping": ["Eliminates manual IT configuration errors", "Ensures highly reproducible server deployments", "Allows scaling infrastructure operations without linearly adding IT headcount"],
        "consulting_category_alignment": ["DevOps Consulting", "IT Infrastructure Automation"]
    },
    "comptia": {
        "key_capabilities_proven": ["Engineered tools to parse Windows Event Logs", "Developed robust command-line interfaces", "Managed data indexing and exposure for analytics"],
        "business_value_mapping": ["Automates cybersecurity audits", "Streamlines incident response data pipelines", "Turns raw system logs into actionable intelligence"],
        "consulting_category_alignment": ["Security Engineering Consulting", "Backend Software Consulting"]
    },
    "elite_quick": {
        "key_capabilities_proven": ["Architected complex ETL data pipelines (Medallion architecture)", "Built REST APIs for pipeline management", "Handled database state, schema drift, and job scheduling"],
        "business_value_mapping": ["Centralizes disparate data sources for BI", "Automates data ingestion to reduce manual analyst labor", "Builds scalable data infrastructure for enterprise analytics"],
        "consulting_category_alignment": ["Data Engineering Consulting", "Backend Architecture Consulting"]
    },
    "elite_dashboard": {
        "key_capabilities_proven": ["Built modern Single Page Applications (SPAs) using Vue 3 and Vite", "Implemented client-side routing and state management", "Integrated frontend frameworks with Bootstrap"],
        "business_value_mapping": ["Provides intuitive visual analytics interfaces", "Enables rapid prototyping of user experiences", "Increases user engagement through modern UI/UX"],
        "consulting_category_alignment": ["Frontend Engineering Consulting", "Full-Stack Development"]
    },
    "elite_data_lab": {
        "key_capabilities_proven": ["Established isolated environments for Data Science and Telemetry", "Separated domain-specific research from core platform engineering"],
        "business_value_mapping": ["Enables safe, sandboxed data exploration without impacting production", "Accelerates R&D for data insights"],
        "consulting_category_alignment": ["Data Science Consulting", "Data Engineering Consulting"]
    },
    "student-fraud-id": {
        "key_capabilities_proven": ["Built specialized fraud detection logic using Python and SQLModel", "Integrated with complex Higher Ed systems (Ellucian Banner, Target-X, Axiom)", "Designed relational database schemas for application tracking"],
        "business_value_mapping": ["Saves institutions money by automatically detecting application fraud", "Bridges data gaps between disparate educational CRMs", "Automates high-risk application flagging"],
        "consulting_category_alignment": ["EdTech Consulting", "Systems Integration Consulting"]
    },
    "pipeline": {
        "key_capabilities_proven": ["Architected a modular processing framework (Slalom)", "Implemented advanced TDD and architecture testing (pytest-archon)", "Designed modular registration and plugin patterns"],
        "business_value_mapping": ["Standardizes enterprise development workflows", "Ensures high code quality and testability across teams", "Reduces technical debt through rigid architectural design"],
        "consulting_category_alignment": ["Software Architecture Consulting", "Backend Engineering"]
    },
    "enigma": {
        "key_capabilities_proven": ["Implemented complex Domain Driven Design (DDD) in Node/TypeScript", "Built custom cryptographic/simulation engines (Plugboard, Reflector)", "Engineered robust domain error handling hierarchies"],
        "business_value_mapping": ["Encapsulates complex business rules into testable domains", "Ensures high-fidelity simulation of physical/logical systems", "Produces highly maintainable and type-safe backend systems"],
        "consulting_category_alignment": ["Backend Software Consulting (Node/TS)", "Domain Driven Design"]
    },
    "tellurion": {
        "key_capabilities_proven": ["Developed AI agent orchestration systems and protocols", "Engineered semantic parsing and NLP pipelines", "Managed instance-based state and process isolation (Tmux Wrapper)"],
        "business_value_mapping": ["Automates complex, multi-step workflows using AI agents", "Unlocks value from unstructured data via semantic search platforms", "Pioneers next-generation human-computer interaction models"],
        "consulting_category_alignment": ["AI/ML Engineering Consulting", "Advanced Automation Consulting"]
    }
}

def update_all_audits():
    count = 0
    for json_path in DATA_DIR.glob("*.json"):
        project_name = json_path.stem
        
        if project_name not in INSIGHTS:
            continue
            
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        insights = INSIGHTS[project_name]
        data["key_capabilities_proven"] = insights["key_capabilities_proven"]
        data["business_value_mapping"] = insights["business_value_mapping"]
        data["consulting_category_alignment"] = insights["consulting_category_alignment"]
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
            
        print(f"Updated {project_name}.json")
        count += 1
        
    print(f"Successfully updated {count} files.")

if __name__ == "__main__":
    update_all_audits()
