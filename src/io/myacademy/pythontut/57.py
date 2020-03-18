#Please download the file in the attachment and use Python to print out its content.

#Expected output:

#{'employees': [{'firstName': 'John', 'lastName': 'Doe'},
#               {'firstName': 'Anna', 'lastName': 'Smith'},
#               {'firstName': 'Peter', 'lastName': 'Jones'}],
# 'owners': [{'firstName': 'Jack', 'lastName': 'Petter'},
#            {'firstName': 'Jessy', 'lastName': 'Petter'}]}

from pprint import  pprint
import json

with open("../../../../resources/dict.json","r") as f:
    l = json.load(f)  #this loads from the file pointer
    pprint(l)


#Alternatively can use json.loads(f.read()) this loads from a string,