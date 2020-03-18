#Store the dictionary in a json file.


import json

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

#help(json.dump)
with open("../../../../resources/dict.json","w") as f:
    json.dump(d,f,indent=3)


