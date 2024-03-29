#Create an English to Portuguese translation program.

#The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source.
# In addition, return the message "We couldn't find that word!" when the user enters a word that is not in the dictionary.
# Also, make the program non case-sensitive meaning that for example, both earth and Earth should return the translation correctly for that word.
import string

d = dict(weather = "clima", earth = "terra", rain = "chuva")

#Expected output:

#Enter word: hello
#We couldn't find that word!
def vocab(word):
    try:
        return (d[str.lower(word)])
    except KeyError:
        return "That word doesn't exist!"

w = input("Enter word: ")
print(vocab(w))