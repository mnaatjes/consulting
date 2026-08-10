import os
import json
import sys
import datetime
import subprocess
import tempfile
import re
from pathlib import Path

DATA_DIR = Path("data")

def init_env():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

def clone_repo(url, dest_dir):
    try:
        subprocess.run(["git", "clone", "--depth", "1", url, dest_dir], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error cloning {url}: {e.stderr.decode()}")
        return False

def safe_run_command(cmd, cwd=None):
    try:
        result = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, shell=True)
        return result.stdout.strip().split('\n') if result.stdout else []
    except Exception:
        return []

def get_readme_abstract(path_obj):
    for readme_name in ["README.md", "Readme.md", "readme.md"]:
        readme_path = path_obj / readme_name
        if readme_path.exists():
            try:
                with open(readme_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    abstract = []
                    for line in lines:
                        if len(abstract) > 10 or (abstract and line.startswith('##')):
                            break
                        if line.strip():
                            abstract.append(line.strip())
                    return " ".join(abstract[:5]) # limit to a few lines
            except Exception:
                pass
    return ""

def extract_dependencies(path_obj):
    deps = []
    req_file = path_obj / "requirements.txt"
    if req_file.exists():
        try:
            with open(req_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.split('==')[0].split('>')[0].strip()
                    if line and not line.startswith('#'):
                        deps.append(line)
        except Exception: pass
    
    pkg_file = path_obj / "package.json"
    if pkg_file.exists():
        try:
            with open(pkg_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                deps.extend(list(data.get('dependencies', {}).keys()))
        except Exception: pass
    return deps[:30] # Limit to top 30 to save tokens

def analyze_directory(path):
    core_stack = set()
    infra_ops = set()
    
    path_obj = Path(path)
    if not path_obj.exists():
        return None

    # Core Stack detection
    if (path_obj / "package.json").exists(): core_stack.add("Node.js/NPM")
    if (path_obj / "requirements.txt").exists() or (path_obj / "Pipfile").exists() or (path_obj / "pyproject.toml").exists(): core_stack.add("Python")
    if (path_obj / "go.mod").exists(): core_stack.add("Go")
    if (path_obj / "pom.xml").exists() or (path_obj / "build.gradle").exists(): core_stack.add("Java")
    if (path_obj / "Cargo.toml").exists(): core_stack.add("Rust")
    if (path_obj / "Gemfile").exists(): core_stack.add("Ruby")
    
    # Infra & Ops detection
    if (path_obj / "Dockerfile").exists(): infra_ops.add("Docker")
    if (path_obj / "docker-compose.yml").exists() or (path_obj / "docker-compose.yaml").exists(): infra_ops.add("Docker Compose")
    if (path_obj / ".github" / "workflows").exists(): infra_ops.add("GitHub Actions")
    if (path_obj / ".gitlab-ci.yml").exists(): infra_ops.add("GitLab CI")
    if (path_obj / "Jenkinsfile").exists(): infra_ops.add("Jenkins")
    if list(path_obj.glob("*.tf")): infra_ops.add("Terraform")

    # High-signal Context Extraction
    readme_abstract = get_readme_abstract(path_obj)
    dependencies = extract_dependencies(path_obj)
    
    # Architectural Signatures via grep (limiting lines and filtering noise)
    routes = safe_run_command(r"grep -rE '@(app|router)\.(get|post|put|delete)|app\.(get|post|put|delete)' . 2>/dev/null | grep -v 'node_modules' | grep -v 'venv' | head -n 15", cwd=str(path_obj))
    classes = safe_run_command(r"grep -rE 'class [A-Z]' . 2>/dev/null | grep -v 'venv' | grep -v 'node_modules' | head -n 15", cwd=str(path_obj))
    ci_steps = safe_run_command(r"grep -r 'name:' .github/workflows/ 2>/dev/null | head -n 15", cwd=str(path_obj))
    tree_struct = safe_run_command(r"find . -maxdepth 2 -not -path '*/\.*' -not -path '*/node_modules*' -not -path '*/venv*' 2>/dev/null", cwd=str(path_obj))[:30]

    last_updated = datetime.datetime.fromtimestamp(path_obj.stat().st_mtime).strftime('%Y-%m-%d')
    
    return {
        "core_stack": list(core_stack),
        "infrastructure_and_ops": list(infra_ops),
        "last_updated": last_updated,
        "raw_extracted_context": {
            "readme_abstract": readme_abstract,
            "dependencies": dependencies,
            "api_routes": [r for r in routes if r],
            "data_models_classes": [c for c in classes if c],
            "ci_cd_steps": [s for s in ci_steps if s],
            "folder_structure": [t for t in tree_struct if t]
        }
    }

def process_target(target):
    is_url = target.startswith("http://") or target.startswith("https://")
    project_name = target.split("/")[-1].replace(".git", "")
    
    print(f"Processing {target}...")
    
    info = None
    if is_url:
        with tempfile.TemporaryDirectory() as temp_dir:
            repo_dir = os.path.join(temp_dir, project_name)
            if clone_repo(target, repo_dir):
                info = analyze_directory(repo_dir)
                info['last_updated'] = datetime.datetime.now().strftime('%Y-%m-%d')
    else:
        info = analyze_directory(target)
        
    if not info:
        print(f"Failed to process {target}")
        return

    record = {
        "project_name": project_name,
        "location": target,
        "last_updated": info["last_updated"],
        "status": "Unknown",
        "core_stack": info["core_stack"],
        "infrastructure_and_ops": info["infrastructure_and_ops"],
        "key_capabilities_proven": [],
        "business_value_mapping": [],
        "consulting_category_alignment": [],
        "raw_extracted_context": info["raw_extracted_context"]
    }
    
    output_file = DATA_DIR / f"{project_name}.json"
    with open(output_file, 'w') as f:
        json.dump(record, f, indent=2)
    
    print(f"Saved record to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/project_auditor.py <path_or_url1> [path_or_url2 ...]")
        sys.exit(1)
        
    init_env()
    for target in sys.argv[1:]:
        process_target(target)
