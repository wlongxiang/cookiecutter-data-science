from setuptools import find_packages, setup
import re

VERSIONFILE = "{{ cookiecutter.project_name }}/__init__.py"
with open(VERSIONFILE, "rt") as versionfle:
    verstrline = versionfle.read()
version_re = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(version_re, verstrline, re.M)
if mo:
    ver_str = mo.group(1)
else:
    raise ValueError("Unable to find version string in %s." % (VERSIONFILE,))

# add prod requires to setup so that pip can install dependencies for you
with open("requirements_prod.txt") as f:
    required_pkgs = f.read().splitlines()

setup(
    name='{{ cookiecutter.project_name }}',
    packages=find_packages(),
    version=ver_str,
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
    install_requires=required_pkgs
)
