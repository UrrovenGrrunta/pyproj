# templates.py

MAIN_TEMPLATE = """def main():
    pass
    

if __name__ == "__main__":
    main()
"""

GITIGNORE_TEMPLATE = """__pycache__/
*.pyc
.venv/
.env
"""


def get_readme_template(project_name: str) -> str:
    README_TEMPLATE = f"""## {project_name}

## Description

Add the project description here"""
    return README_TEMPLATE

def get_requirements_template(project_name: str) -> str:
    REQUIREMENTS_TEMPLATE = f"""Requirements for {project_name}
    
"""
    return REQUIREMENTS_TEMPLATE