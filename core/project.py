import shutil
import subprocess

from pathlib import Path

from . import logger


DEFAULT_DIRECTORY = Path("/home/urrovengrrunta/coding/Python/")
TEMPLATE_DIRECTORY = Path(
    "/home/urrovengrrunta/coding/Python/pyproj/templates"
)
DEFAULT_TEMPLATE = "basic"
SUPPORTED_EXTENSIONS = (".py", ".txt", ".md", ".kv")


def create_directory(project_name: str) -> Path:
    project_path = DEFAULT_DIRECTORY / project_name

    logger.info(f"Creating project directory: {project_path}")

    try:
        project_path.mkdir()
    except FileExistsError as error:
        logger.error(f"Project '{project_name}' already exists.")
        raise FileExistsError(
            f"Project '{project_name}' already exists."
        ) from error

    logger.success("Project directory created.")
    return project_path


def copy_template(project_path: Path, template: str) -> None:
    if template == "":
        template = DEFAULT_TEMPLATE

    template_path = TEMPLATE_DIRECTORY / template
    logger.info(f"Copying '{template}' template...")

    if template_path.is_dir():
        shutil.copytree(
            template_path,
            project_path,
            dirs_exist_ok=True,
        )
        logger.success("Template copied.")
        return

    existing_templates = []

    for template_directory in TEMPLATE_DIRECTORY.iterdir():
        if template_directory.is_dir():
            existing_templates.append(template_directory.name)

    logger.error(f"Template '{template}' was not found.")
    raise FileNotFoundError(
        f"No template '{template}' found.\n"
        f"Available templates: {existing_templates}"
    )


def replace_placeholders(
    project_path: Path,
    project_name: str,
) -> None:
    logger.info("Replacing template placeholders...")

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

    logger.success("Template placeholders replaced.")


def create_venv(project_path: Path) -> None:
    logger.info("Creating virtual environment...")

    subprocess.run(
        ["python3", "-m", "venv", ".venv"],
        cwd=project_path,
        check=True,
    )

    logger.success("Virtual environment created.")


def install_dependencies(project_path: Path) -> None:
    venv_python_path = project_path / ".venv/bin/python"
    requirements_path = project_path / "requirements.txt"

    if not requirements_path.is_file():
        logger.warning(
            "requirements.txt was not found. "
            "Dependency installation skipped."
        )
        return

    logger.info("Installing dependencies...")

    subprocess.run(
        [
            str(venv_python_path),
            "-m",
            "pip",
            "install",
            "-r",
            str(requirements_path),
        ],
        cwd=project_path,
        check=True,
    )

    logger.success("Dependencies installed.")


def generate_project(
    project_name: str,
    template: str = DEFAULT_TEMPLATE,
) -> None:
    logger.info(f"Generating project '{project_name}'...")

    project_path = create_directory(project_name)
    copy_template(project_path, template)
    replace_placeholders(project_path, project_name)
    create_venv(project_path)
    install_dependencies(project_path)

    logger.success(f"Project created successfully: {project_path}")