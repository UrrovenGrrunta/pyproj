# pyproj

`pyproj` is a small command-line project generator written in Python.

It creates a new project directory, copies a selected template, and replaces template placeholders such as `{{PROJECT_NAME}}` with the actual project name.

> **Status:** Alpha. The project is still in development, and some flags and templates are not implemented yet.

## Current features

- Create a project in the default Python projects directory
- Copy files from a project template
- Use the `basic` template by default
- Replace `{{PROJECT_NAME}}` inside supported text files
- Parse short and long command-line flags
- Detect unknown flags
- Prevent overwriting an existing project directory

## Usage

Run the generator with a project name:

```bash
python main.py my_project
```

The project will be created using the `basic` template.

Planned template flags:

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

| Short | Long | Purpose |
|---|---|---|
| `-tg` | `--telegram` | Use the Telegram bot template |
| `-kv` | `--kivy` | Use the KivyMD template |
| `-gh` | `--github` | Create a GitHub repository |
| `-pb` | `--public` | Set GitHub repository visibility to public |
| `-pv` | `--private` | Set GitHub repository visibility to private |

Telegram, KivyMD, and GitHub functionality are currently being developed.

## Project structure

```text
pyproj/
├── main.py
├── core/
│   ├── parser.py
│   ├── project.py
│   ├── github.py
│   ├── templates.py
│   └── cli.py
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
```

The generator currently replaces `{{PROJECT_NAME}}` in supported file types such as:

- `.py`
- `.txt`
- `.md`
- `.kv`

## Requirements

- Python 3.10 or newer
- No third-party dependencies are currently required

## Roadmap

- Finish the Telegram bot template
- Add the KivyMD template
- Create virtual environments automatically
- Initialise Git repositories
- Add optional GitHub repository creation
- Improve command-line validation and error handling

## Author

Created by [UrrovenGrrunta](https://github.com/UrrovenGrrunta).
