#Please download the json file in the attachment and use Python to add a new employee
# to the content of the file so that the file looks like in the expected output below.


import json

with open("../../../../resources/dict.json","r+") as f:
    l = json.load(f)
    l["employees"].append({"firstName":"Trina","lastName":"Dey"})
    f.seek(0)
    json.dump(l,f,indent=3)