import core.project as project
import core.parser as parser
import core.logger as logger

from subprocess import CalledProcessError

def main():
    try:
        project_name, options = parser.parse_flags()
        template = "basic"
        if "telegram" in options and "kivymd" in options:
            raise ValueError("Telegram and Kivy templates cannot be used together.")
        for template_option in options:
            match template_option:
                case "telegram":
                    template = "telegram"
                case "kivymd":
                    template = "kivymd"
        project.generate_project(project_name, template)
    except (ValueError, FileExistsError, FileNotFoundError, CalledProcessError) as error:
        logger.error(str(error))

if __name__ == "__main__":
    main()