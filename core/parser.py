import sys

def parse_flags():
    project_name = sys.argv[1]
    project_flags = sys.argv[2:]
    options = []
    allowed_flags = {
        "-tg": "telegram",
        "--telegram": "telegram",

        "-kv": "kivy",
        "--kivy": "kivy",

        "-gh": "github",
        "--github": "github",

        "-pb": "visibility: public",
        "--public": "visibility: public",

        "-pv": "visibility: private",
        "--private": "visibility: private",
    }

    for flag in project_flags:
        if flag in allowed_flags:
            options.append(allowed_flags[flag])
        else:
            print(f"Error, unknown flag {flag}")
    return project_name, options