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

class Level():
    def __init__(self, level = 1):
        self.level = level

    def go_deeper(self):
        self.level = self.level + 1

    def come_up(self):
        self.level = self.level - 1




def get_curr_level(json_data):
    current_file = json_data
    list_i = current_file["children"]
    find_children(list_i)

def find_children(my_children):

    for i in my_children:
        print(i["name"])
        print(level_finder.level)
        
        if i["children"]:
            level_finder.go_deeper()
            get_curr_level(i)
        

    level_finder.come_up()

def find_children2(json_step):
    next_step = json_step["children"]
    return next_step

def read_json(json_file):
    with open(json_file) as file:
        json_data = json.load(file)
        get_curr_level(json_data)

if __name__ == '__main__':
    #get_dictionary_word_list(args.filename, args.location)
    level_finder = Level()
    read_json(args.filename)


        