import core.project as project
import core.parser as parser


def main():
    project_name, options = parser.parse_flags()
    template = "basic"
    for template_option in options:
        match template_option:
            case "telegram":
                template = "telegram"
            case "kivy":
                template = "kivy"
    project.generate_project(project_name, template)

if __name__ == "__main__":
    main()