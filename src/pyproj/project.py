import shutil
import subprocess
import os

from pathlib import Path

from . import logger


DEFAULT_DIRECTORY = Path("/home/urrovengrrunta/coding/Python/")
TEMPLATE_DIRECTORY = Path(
    "/home/urrovengrrunta/coding/Python/pyproj/templates"
)
DEFAULT_TEMPLATE = "basic"
SUPPORTED_EXTENSIONS = (".py", ".txt", ".md", ".kv", ".toml")

project_exists = False


def create_directory(project_name: str) -> Path:
    global project_exists

    project_path = DEFAULT_DIRECTORY / project_name

    try:
        logger.info(f"Creating project directory: {project_path}")
        project_path.mkdir()
        logger.success("Project directory created.")
    except FileExistsError:
        project_exists = True
        logger.error(f"Project '{project_name}' already exists.")
        open_project(project_path)
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


def sync_project(project_path: Path) -> None:
    pyproject_path = project_path / "pyproject.toml"

    if not pyproject_path.is_file():
        logger.warning(
            "pyproject.toml was not found. "
            "Environment setup skipped."
        )
        return

    logger.info("Syncing project environment with uv...")
    env = os.environ.copy()
    env.pop("VIRTUAL_ENV", None)
    subprocess.run(
        ["uv", "sync"],
        cwd=project_path,
        env=env,
        check=True,
    )

    logger.success("Project environment synced.")


def open_in_code(project_path: Path) -> None:
    subprocess.Popen(
        ["code", str(project_path)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def open_project(project_path: Path) -> None:
    subprocess.run(["cd", project_path], cwd=project_path, check=True)


def generate_project(
    project_name: str,
    template: str = DEFAULT_TEMPLATE,
) -> None:
    logger.info(f"Generating project '{project_name}'...")

    project_path = create_directory(project_name)
    if not project_exists:
        copy_template(project_path, template)
        replace_placeholders(project_path, project_name)
        sync_project(project_path)
        open_in_code(project_path)
    else:
        sync_project(project_path)
        open_in_code(project_path)
    logger.success(f"Project created successfully: {project_path}")
