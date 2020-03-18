#write a script that extracts the alphabets from the txt files and adds them to a list and print the list

import os

l= []
if os.path.exists("../../../../resources/letters"):
    for r,d,f in os.walk("../../../../resources/letters"):
        for filepath in f:
            with  open(os.path.join(r,filepath),"r") as a:
                l.append(a.readline())
    print(sorted(l))


#Alternative
import glob
l =[]
file_list = glob.glob("../../../../resources/letters/*.txt")

for fileName in file_list:
    with open(fileName, "r") as file:
        l.append(file.readline().strip("\n"))
print(sorted(l))