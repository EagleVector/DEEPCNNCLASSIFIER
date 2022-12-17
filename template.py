#CREATING THE BASIC SKELETON FOR THE PROJECT
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ') #logging level set to info level

package_name = "DeepClassifier"

#creating all the necessary files for project in one go
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    f"src/{package_name}/config/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",                      #testing class and functions
    "tests/integration/__init__.py",               #testing components in pipeline
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",                                   #pypi setup configuration
    "pyproject.toml",                              #pypi setup
    "tox.ini",
    "research/trials.ipynb"
]                           

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)   #splits the diectory with the file
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}") #creating directory

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #create file only when its an empty file otherwise skip: donot overwrite
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}") #creating files

    else:
        logging.info(f"{filename} already exists")

#Necessary skelton created