import yaml
from yaml.loader import SafeLoader
from directorymaker_json import Level
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--filename", default = 'examples/structureexample.yaml', type = str)
parser.add_argument("--location", default = str(os.getcwd()), type = str)

args = parser.parse_args()

def search_children(json_data):

    """
    Check if children data exists, and send it to make_dir to
    write the directories
    """

    if json_data['children']:
        level_finder.deeper_dir()

        for i in json_data['children']:
            make_dir(i['name'])
            search_children(i)

        level_finder.higher_dir()

def read_yaml(yaml_file):

    """
    Load the json file, and start initial search for 'children' folders
    """

    with open('examples/structureexample.yml', 'r') as f:
        yaml_data = list(yaml.load_all(f, Loader=SafeLoader))
        print(yaml_data)

    print(yaml_data[0]['folder2'])


if __name__ == '__main__':
    level_finder = Level()
    read_yaml(args.filename)
