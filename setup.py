from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ascii_live_menu",
    version="0.19.0425",
    author="Kelven Vilela",
    author_email="kelvenserejo@gmail.com",
    description="Description",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KelvenVS/ASCII_Live_Menu..git"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.11',
)