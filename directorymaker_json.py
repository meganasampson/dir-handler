import os
from pathlib import Path
import argparse
import json


filelist = []
finalstructure = []


parser = argparse.ArgumentParser()
parser.add_argument("--filename", default = 'examples/structureexample.json', type = str)
parser.add_argument("--location", default = str(os.getcwd()), type = str)

args = parser.parse_args()


def folder_maker(filelist, location):
    """
    loops through file structure list and makes folders based on ├── symbol
    """
    os.chdir(location)

    level = 1

    for i in range(len(filelist)):

        if "├──" not in filelist[i]:
            #checks where the next folder should be based on current level
            level2 = filelist[i-1].count("├──")

            if level2 == level:
                #make folder in same directory
                os.makedirs(filelist[i])

            elif level2 > level:
                #moves DOWN next directory and makes folder in there
                cwd = Path(os.getcwd())
                foldername = Path(filelist[i-2])
                newpath = cwd/foldername
                os.chdir(newpath)
                os.makedirs(filelist[i])
                #make new level the current level
                level = level + 1

            elif level2 < level:
                for j in range(level - level2):
                    #moves UP to the correct directory and makes folder there
                    cwd = Path(os.getcwd())
                    foldername = Path("..")
                    newpath = cwd/foldername
                    os.chdir(newpath)
                os.makedirs(filelist[i])
                #make new level the current level
                level = level2

def dir_maker(foldername):
    os.makedirs(foldername)

def find_children(json_step):
    next_step = json_step["children"]
    return next_step

def read_json(json_file):
    with open(json_file) as file:
        json_data = json.load(file)
    if json_data["children"]:
        json_data = find_children(json_data)


if __name__ == '__main__':
    #get_dictionary_word_list(args.filename, args.location)
    read_json(args.filename)



        