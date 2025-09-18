import json

json_file = "examples/loops.json"
with open(json_file, 'r') as f:
    folder_data = json.load(f)

print(folder_data)

myloops = {"x":"3", "y":"2"}

for i in folder_data:
    print(i)
    res = i.translate(str.maketrans(myloops))
    print(res)


for i in folder_data:
    for key in myloops.keys():
        if key in i:
            print(f"{i} contains an {key}")
        else:
            print(f"{i} DOES NOT contain an {key}")

for i in folder_data:
    for key in myloops.keys():
        if key in i:
            value = int(myloops[key])
            for i in range(int(value)):
                print(f"printing {i}")
        else:
            print(f"{i} DOES NOT contain an {key}")