#Filter the dictionary by removing all items with a value of greater than 1.

d = {"a": 1, "b": 2, "c": 3}

#Sol
dict_new = dict((x,y) for x,y in d.items() if y <=1)
print(dict_new)