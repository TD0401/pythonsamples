#Create a script that generates a file where all letters of English alphabet are listed three in each line. The inside of the text file would look like:

#abc
#def
#ghi

#and so on.

#Sol
import string
letters = string.ascii_lowercase + " "
with open("../../../../resources/alpha3.txt","w") as file:
    for letter1, letter2,letter3 in zip(letters[0::3], letters[1::3] , letters[2::3]):
        file.write(letter1+letter2 + letter3 + "\n")
