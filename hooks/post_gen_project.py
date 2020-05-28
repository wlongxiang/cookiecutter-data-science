"""
Borrowed from cookiecutter-django: https://github.com/pydanny/cookiecutter-django
"""

import os
from rich.console import Console

# for fancy print
console = Console()


def remove_azure_pipeline_yaml_file():
    os.remove("azure-pipelines.yml")


def main():
    if "{{ cookiecutter.use_azure_pipeline }}".lower() == "n":
        remove_azure_pipeline_yaml_file()
    console.print("Your project is initiated successfully, enjoy the journey!", style="bold green")


if __name__ == "__main__":
    main()
