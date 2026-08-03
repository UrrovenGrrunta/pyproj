# pyproj

pyproj is a small command-line project generator written in Python.

It creates a new project directory, copies a selected template, replaces template placeholders such as {{PROJECT_NAME}}, creates a virtual environment, and installs template dependencies when a requirements.txt file is present.

> **Status:** Alpha. The project is still in development, and GitHub repository creation is not implemented yet.

## Current features

• Create a project in the default Python projects directory

• Copy files from a selected project template

• Use the basic template by default

• Support basic, telegram, and kivymd templates

• Replace {{PROJECT_NAME}} inside supported text files

• Create a .venv virtual environment

• Install dependencies from requirements.txt

• Parse short and long command-line flags

• Detect unknown flags

• Prevent conflicting template flags

• Prevent overwriting an existing project directory

• Show coloured progress, success, warning, and error messages

• Hide unnecessary tracebacks for expected user errors

## Usage

Run the generator with a project name:

```bash
python main.py my_project
```

The project will be created using the basic template.

Use a different template:

```bash
python main.py my_bot --telegram
python main.py my_app --kivy
```

Short versions:

```bash
python main.py my_bot -tg
python main.py my_app -kv
```

## Available flags

|Short|Long        |Purpose                                                |
|-----|------------|-------------------------------------------------------|
|`-tg`|`--telegram`|Use the Telegram bot template                          |
|`-kv`|`--kivy`    |Use the KivyMD template                                |
|`-gh`|`--github`  |Create a GitHub repository *(planned)*                 |
|`-pb`|`--public`  |Set GitHub repository visibility to public *(planned)* |
|`-pv`|`--private` |Set GitHub repository visibility to private *(planned)*|

Telegram and KivyMD templates are available. GitHub repository creation and visibility flags are still being developed.

## Project structure

```text
pyproj/
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
create_venv()
        ↓
install_dependencies()
```

The generator replaces {{PROJECT_NAME}} in supported file types:

• .py
• .txt
• .md
• .kv

If the selected template contains a requirements.txt file, its dependencies are installed inside the newly created virtual environment.

## Requirements

• Python 3.10 or newer
• colorama 0.4.6 or newer

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