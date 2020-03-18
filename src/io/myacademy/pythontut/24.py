#Please complete the script so that it prints out the expected output.


d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

#Sol
for x,y in d.items():
    print(x + " has value " + str(y))


#Alternative
#print(x,"has value",y)