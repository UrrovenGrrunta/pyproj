import os 

from pathlib import Path

main_directory = str(Path(__file__).resolve().parent.parent.parent)
project_name = 'test'

def create_project_linux(project_name): # Function to create project directory in Linux systems
    print(main_directory + "/" + project_name)

def create_project_win(project_name): # Function to create project directory in Windows
    print(main_directory + "\\"+ project_name)

create_project_linux(project_name)
create_project_win(project_name)