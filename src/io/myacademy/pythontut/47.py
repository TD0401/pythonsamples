#write a script that extracts the alphabets from the txt files and adds them to a list only if they belong to string
# python and print the list

import glob
l =[]
file_list = glob.glob("../../../../resources/letters/*.txt")

for fileName in file_list:
    with open(fileName, "r") as file:
        a = (file.readline().strip("\n"))
        if("python".__contains__(a)):
            l.append(a)

print(sorted(l))