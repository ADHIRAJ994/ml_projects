from setuptools import find_packages,setup
from typing import List
# This func will return the list of requirements
def get_requirements(file_path) -> List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements
setup(
    name="ml_project",
    version="0.0.1",
    author="Adhiraj Chakravorty",
    author_email="youradhi20@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)