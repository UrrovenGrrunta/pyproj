## File containing logic for creating GH repo
import subprocess
from pathlib import Path
from urllib.request import Request, urlopen
from json import dumps, loads
from os import environ

from pyproj import logger




def init_git(project_path: Path):
    logger.info("Initializing Git repository...")
    subprocess.run(
        ["git", "init"],
        cwd=project_path,
        check=True,
    )
    


def git_add(project_path: Path):
    logger.info("Adding files for commit...")
    subprocess.run(
        ["git", "add", "."],
        cwd=project_path,
        check=True,
    )


def git_initial_commit(project_path: Path):
    logger.info("Initial commit")
    subprocess.run(
        ["git", "commit", "-m", '"Initial Commit"'],
        cwd=project_path,
        check=True,
    )

## GitHub API (kinda)
def create_github_repo(project_name: str, private:bool = False) -> None:
    GITHUB_TOKEN = environ.get("GITHUB_TOKEN")
    