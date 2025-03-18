import os
from pathlib import Path
import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument("--filename", default = 'examples/structureexample.json', type = str)
parser.add_argument("--location", default = str(os.getcwd()), type = str)

args = parser.parse_args()

class Level():
    def __init__(self, level = 0):
        self.level = level

    def go_deeper(self):
        #print("number go up")
        self.level = self.level + 1

    def come_up(self):
        #print("number go down")
        self.level = self.level - 1


def see_children(json_data):
    print(level_finder.level)
    if json_data['children']:
        #print(level_finder.level)
        level_finder.go_deeper()
        for i in json_data['children']:
            print(i['name'])
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