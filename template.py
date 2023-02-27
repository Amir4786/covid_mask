import os
from pathlib import Path
import logging

logging.basicConfig(level= logging.INFO,
                          format= "[%(asctime)s: %(levelname)s]:%(message)s")
while True:
    project_name= input("Enter the Project Name: ")
    if project_name !="":
        break
logging.info("Project Name is: {}".format(project_name))

list_of_files = [
                ".github/workflows/.gitkeep",
                f"src/{project_name}/__init__.py",
                f"tests/__init__.py",
                f"tests/unit/__init__.py",
                f"tests/integration/__init__.py",
                "init_setup.sh",
                "requirements.txt",
                "requiements_dev.txt",
                "setup.py",
                "pyproject.toml",
                "setup.cfg",
                "tox.ini"
]
for filepath in list_of_files:
    filepath= Path(filepath)
    filedir, filename= os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info("Creating a Directory at: {} for file: {}".format(filedir, filename))
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info("Creating a new file: {} at path: {}".format(filename, filepath))
    else:
        logging.info("File: {} is already exist at path: {}".format(filename, filepath))