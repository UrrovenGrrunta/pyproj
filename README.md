# pyproj

**Project status: Done as for version 2.0**

pyproj is a small command-line project generator written in Python and managed with [uv](https://docs.astral.sh/uv/).

It creates a new project directory, copies a selected template, replaces template placeholders such as `{{PROJECT_NAME}}`, and runs `uv sync` to create the virtual environment and install the template dependencies.

> **Status:** Alpha. The project is still in development.

## Current features

• Create a project in the default Python projects directory

• Copy files from a selected project template

• Use the basic template by default

• Support basic, telegram, and kivymd templates

• Replace `{{PROJECT_NAME}}` inside supported text files

• Manage generated project environments and dependencies with uv

• Parse short and long command-line flags

• Detect unknown flags

• Prevent conflicting template flags

• Prevent overwriting an existing project directory

• Show coloured progress, success, warning, and error messages

• Hide unnecessary tracebacks for expected user errors

## Setup

Install uv, then sync the repository:

```bash
uv sync
```

## Usage

Run the generator with a project name:

```bash
uv run python main.py my_project
```

Use a different template:

```bash
uv run python main.py my_bot --telegram
uv run python main.py my_app --kivy
```

Short versions:

```bash
uv run python main.py my_bot -tg
uv run python main.py my_app -kv
```

## Available flags

|Short|Long        |Purpose                                                |
|-----|------------|-------------------------------------------------------|
|`-tg`|`--telegram`|Use the Telegram bot template                          |
|`-kv`|`--kivy`    |Use the KivyMD template                                |
|`-gh`|`--github`  |Create a GitHub repository *(planned)*                 |
|`-pb`|`--public`  |Set GitHub repository visibility to public *(planned)* |
|`-pv`|`--private` |Set GitHub repository visibility to private *(planned)*|

## Project structure

```text
pyproj/
├── pyproject.toml
├── main.py
├── core/
│   ├── parser.py
│   ├── project.py
│   └── logger.py
└── templates/
    ├── basic/
    ├── telegram/
    └── kivymd/
```

## How generation works

```text
create_directory()
        ↓
copy_template()
        ↓
replace_placeholders()
        ↓
uv sync
```

Each template contains its own `pyproject.toml`. After the template is copied and placeholders are replaced, `uv sync` creates `.venv` and installs the declared dependencies.

## Requirements

• Python 3.10 or newer

• uv

## Roadmap

• Initialize local Git repositories

• Add optional GitHub repository creation

• Support public and private GitHub repository visibility

## Report an issue

[Report an issue](https://github.com/UrrovenGrrunta/pyproj/issues/new).

## Author

Created by UrrovenGrrunta.

## Contact me

[Contact me on Discord](https://discordapp.com/users/492016021545287690).

[Contact me on Telegram](https://t.me/uRR0vengRRunta).
