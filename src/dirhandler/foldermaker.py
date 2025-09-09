import os
import json
import argparse
import pathlib
from enum import Enum

"""define the arguments for making folders"""
parser = argparse.ArgumentParser()
parser.add_argument('-x', action='store_true',
                    help="takes example file structures when present")
parser.add_argument("--filename", default = 'examples/nestedtstruc.json', 
                    type = str,
                    help="path to json file to read structure")
parser.add_argument("--location", default = '.', 
                    type = str,
                    help="path to create folders in")

args = parser.parse_args()

example_json = {"simpleexample":"example/simplestruc.json",
                "nestedexample":"example/nestedstrc.json"}

def create_folder_structure(base_path, structure):

    if isinstance(structure, list):
        for folder_name in structure:
            path = os.path.join(base_path, folder_name)
            os.makedirs(path, exist_ok=True)
            print(f"Created directory: {path}")
    elif isinstance(structure, dict):
        for folder_name, sub_structure in structure.items():
            path = os.path.join(base_path, folder_name)
            os.makedirs(path, exist_ok=True)
            print(f"Created directory: {path}")
            create_folder_structure(path, sub_structure)
    elif isinstance(structure, str):
        path = base_path+"/"+structure+".txt"
        f = open(path, "w")
        f.close

def start(x=args.x, filename=args.filename, location=args.location):

    if x == True:
        base_dir = pathlib.Path(__file__).parent.resolve() # change eventually __file__ bad...
        json_file = os.path.join(base_dir, filename)
    else:
        json_file = filename

    with open(json_file, 'r') as f:
        folder_data = json.load(f)

    os.chdir(location)

    create_folder_structure('.', folder_data)
    print("Folder structure created successfully!")
