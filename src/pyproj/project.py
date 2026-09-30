import shutil
import subprocess
import os

from pathlib import Path

from pyproj import logger
from pyproj import github

# Default location where generated projects are created.
DEFAULT_DIRECTORY = Path("/home/urrovengrrunta/coding/Python/")

# Directory containing all available project templates.
TEMPLATE_DIRECTORY = Path(
    "/home/urrovengrrunta/coding/Python/pyproj/templates"
)

DEFAULT_TEMPLATE = "basic"

# Only files with these extensions are searched for template placeholders.
SUPPORTED_EXTENSIONS = (".py", ".txt", ".md", ".kv", ".toml")

# Tracks whether the requested project directory already exists.
# Used by generate_project() to avoid overwriting an existing project.
project_exists = False


def create_directory(project_name: str) -> Path:

    project_path = DEFAULT_DIRECTORY / project_name

    try:
        logger.info(f"Creating project directory: {project_path}")
        project_path.mkdir()
        logger.success("Project directory created.")
    except FileExistsError:
        logger.error(f"Project '{project_name}' already exists.")
        raise
        

    return project_path


def copy_template(project_path: Path, template: str) -> None:
    # Fall back to the basic template when no template is specified.
    if template == "":
        template = DEFAULT_TEMPLATE

    template_path = TEMPLATE_DIRECTORY / template
    logger.info(f"Copying '{template}' template...")

    if template_path.is_dir():
        # Copy the selected template into the newly created project directory.
        shutil.copytree(
            template_path,
            project_path,
            dirs_exist_ok=True,
        )
        logger.success("Template copied.")
        return

    # Build a list of valid templates for a more useful error message.
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

    # Search template files recursively and replace placeholders such as
    # {{PROJECT_NAME}} with values belonging to the generated project.
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

    # uv cannot sync a project without its pyproject.toml.
    if not pyproject_path.is_file():
        logger.warning(
            "pyproject.toml was not found. "
            "Environment setup skipped."
        )
        return

    logger.info("Syncing project environment with uv...")

    # pyproj itself may be running inside a virtual environment.
    # Remove VIRTUAL_ENV so the generated project gets its own .venv
    # instead of inheriting pyproj's environment.
    env = os.environ.copy()
    env.pop("VIRTUAL_ENV", None)

    subprocess.run(
        ["uv", "sync"],
        cwd=project_path,
        env=env,
        check=True,
    )
    logger.success("Project environment synced.")


def init_git_repo(project_path: Path) -> None:
    github.init_git(project_path)
    github.git_add(project_path)
    github.git_initial_commit(project_path)
    logger.success("Local Git repository initialized and commited")



def open_in_code(project_path: Path) -> None:
    # Open the generated project in VS Code without blocking pyproj.
    subprocess.Popen(
        ["code", str(project_path)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def generate_project(
    project_name: str,
    template: str = DEFAULT_TEMPLATE,
) -> None:
    logger.info(f"Generating project '{project_name}'...")

    project_path = create_directory(project_name)
    copy_template(project_path, template)
    replace_placeholders(project_path, project_name)
    sync_project(project_path)
    init_git_repo(project_path)
    open_in_code(project_path)

    logger.success(f"Project created successfully: {project_path}")