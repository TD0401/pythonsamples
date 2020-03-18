#Create a function that takes any string as input and returns the number of words for that string.

import string
def countWords(s):
    print("--------------")
    print(len(s.split(" ")))

s = input("Input a sentence - ")
countWords(s)