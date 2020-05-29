"""
Borrowed from cookiecutter-django: https://github.com/pydanny/cookiecutter-django
"""

import os
import shutil


def remove_azure_pipeline_yaml_file():
    os.remove("azure-pipelines.yml")


def remove_mlflow_dir():
    shutil.rmtree("mlflow")


def main():
    if "{{ cookiecutter.use_azure_pipeline }}".lower() == "n":
        remove_azure_pipeline_yaml_file()

    if "{{ cookiecutter.use_mlflow }}".lower() == "n":
        remove_mlflow_dir()

    print("Your project {{ cookiecutter.project_name }} is initiated successfully, enjoy the journey!")


if __name__ == "__main__":
    main()
