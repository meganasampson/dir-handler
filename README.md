# dir-handler

## Installation
- Create and activate virutal environment
```
python -m venv dirhandler
source dirhandler/bin/activate
```

- Install requirements
```
pip install -r requirements.txt
```

**Example Usage**  

Makes a directory structure specified in "path/to/structure.json" in the "directories" folder:
```
python directorymaker_json.py --filename "path/to/structure.json"  --location "directories"
```

**Options**
- --filename : the file to read the directory structure from, default = 'examples/structureexample.json
- --location : the directory in which generated directories will appear, default = current directory
