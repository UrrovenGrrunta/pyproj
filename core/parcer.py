import sys

sys_args = sys.argv

project_name = sys_args[1]
project_flags = sys_args[2:]
optinons = []
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


print(f"Creating project: {project_name}")

for flag in project_flags:
    if flag in allowed_flags:
        optinons.append(allowed_flags[flag])
    if flag not in allowed_flags:
        print(f"Error, unknown flag {flag}")

print(f"Found flags: {optinons}")