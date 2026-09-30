## File containing logic for creating GH repo
import subprocess
import os ## ???

from pathlib import Path

MAIN_PATH = Path(__file__).ressolve().parent.parent


def init_github_repo(root_path: Path):
  
