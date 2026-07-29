# project.py
import shutil

from pathlib import Path

DEFAULT_DIRECTORY = Path("/home/urrovengrrunta/coding/Python/")
TEMPLATE_DIRECTORY = Path("/home/urrovengrrunta/coding/Python/pyproj/templates")
DEFAULT_TEMPLATE = "basic"
SUPPORTED_EXTENSIONS = (".py", ".txt", ".md", ".kv")

def create_directory(project_name: str):
    project_path = DEFAULT_DIRECTORY / project_name

    try:
        project_path.mkdir()
    except FileExistsError as e:
        raise FileExistsError(
            f"Project '{project_name}' already exists."
        ) from e

    return project_path

def copy_template(project_path: Path, template: str):
    if template == "":
        template = DEFAULT_TEMPLATE

    template_path = TEMPLATE_DIRECTORY / template

    if template_path.is_dir():
        shutil.copytree(
            template_path,
            project_path,
            dirs_exist_ok=True
        )
    else:
        existing_templates = []

        for templates in TEMPLATE_DIRECTORY.iterdir():
            if templates.is_dir():
                existing_templates.append(templates.name)

        raise FileNotFoundError(
            f"No template '{template}' found.\n"
            f"Available templates: {existing_templates}"
        )

def replace_placeholders(project_path: Path, project_name: str) -> None:
    for file_path in project_path.rglob("*"):
        if (
            file_path.is_file()
            and file_path.suffix in SUPPORTED_EXTENSIONS
        ):
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            content = content.replace(
                "{{PROJECT_NAME}}",
                project_name,
            )

            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)

def generate_project(project_name: str, template: str = "basic"):
    project_path = create_directory(project_name)
    copy_template(project_path, template)
    replace_placeholders(project_path, project_name)
