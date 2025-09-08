import os
import json
import argparse

"""define the arguments for making folders"""
parser = argparse.ArgumentParser()
parser.add_argument("--filename", default = 'examples/nestedtstruc.json', 
                    type = str,
                    help="path to json file to read structure")
parser.add_argument("--location", default = str(os.getcwd()), 
                    type = str,
                    help="path to create folders in")

args = parser.parse_args()

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

def start():
    json_file = args.filename
    with open(json_file, 'r') as f:
        folder_data = json.load(f)

    create_folder_structure('.', folder_data)
    print("\nFolder structure created successfully!")
