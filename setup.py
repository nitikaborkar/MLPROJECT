from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    '''To get the requirements from the file'''
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='MLPROJECT',
    version='0.1',
    author='Nitika',
    author_email='nitikaborkar@gmail.com',
    packages=find_packages(),  # Finds all packages with an __init__.py file
    install_requires=get_requirements('requirements.txt'),
)
