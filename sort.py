import json
def load_map():
    with open("./cases8/case0.json") as f:
        data = json.load(f)
    

    return data



dictionary = load_map()
sortedlist = [(k,dictionary[k]) for k in sorted(dictionary)]

for name in sortedlist:
    print(name)
