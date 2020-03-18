#Create a script that generates a text file with all letters of English alphabet inside it, one letter per line.

import string

file = open("../../../../resources/alpha.txt","w")
for x in string.ascii_lowercase:
    file.write(x + "\n")
file.close()