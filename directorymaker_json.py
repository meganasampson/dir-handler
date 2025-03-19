import os
from pathlib import Path
import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument("--filename", default = 'examples/structureexample.json', type = str)
parser.add_argument("--location", default = str(os.getcwd()), type = str)

args = parser.parse_args()

class Level():
    def __init__(self, level = 0, previouslvl = 0, directory = os.getcwd(), prev_dif = None):
        self.level = level
        self.previouslvl = previouslvl
        self.directory = directory
        self.prev_dif = prev_dif

    def go_deeper(self):
        self.level = self.level + 1

    def come_up(self):
        self.level = self.level - 1

    def store_lvl(self):
        self.previouslvl = self.level

    def current_level(self, folder_name):
        #self.directory = os.getcwd()
        self.current_level = folder_name
    
    def get_prev_dif(self, curr_level):
        self.prev_dif = curr_level

def make_dir(folder_name):

    #print(folder_name)
    #print(os.getcwd())
    lvl_dif = level_finder.level - level_finder.previouslvl

    if folder_name == 'folder1':
        lvl_dif = 0
        #level_finder.prev_dif = 0
        #FIGURE OUT HOW TO MAKE WORK IN GENERAL
    print(lvl_dif)
    #print(level_finder.prev_dif)

    if lvl_dif > 0:

        for i in range(abs(lvl_dif)):
            os.makedirs(folder_name)
            os.chdir(folder_name)
            print(folder_name)

    elif lvl_dif < 0:
        for i in range(abs(lvl_dif)+1):
            os.chdir('..')
            print(os.getcwd())

        print(folder_name)
        os.makedirs(folder_name)

    elif lvl_dif == 0:
        if level_finder.prev_dif == 0:
            os.chdir("..")
        print(folder_name)
        os.makedirs(folder_name)
        #problem - no movement into folder, so child doesn't know what it belongs to, makes folder 
        os.chdir(folder_name)
        #print("same level")

    else:
        print("what else")
        #os.makedirs(folder_name)

    level_finder.store_lvl()
    level_finder.get_prev_dif(lvl_dif)

def see_children(json_data):

    if json_data['children']:
        level_finder.go_deeper()

        for i in json_data['children']:
            make_dir(i['name'])
            see_children(i)

        level_finder.come_up()

def read_json(json_file):

    with open(json_file) as file:
        json_data = json.load(file)
        see_children(json_data)


if __name__ == '__main__':
    #get_dictionary_word_list(args.filename, args.location)
    level_finder = Level()
    read_json(args.filename)

