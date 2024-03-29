#Create an English to Portuguese translation program.

#The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source.
# In addition, try to return the message "We couldn't find that word!" when the user enters a word that is not in the dictionary.

d = dict(weather = "clima", earth = "terra", rain = "chuva")

#Expected output:

#Enter word: hello
#That word doesn't exist!


i = input("Enter word: ")
if not d.keys().__contains__(i):
    print("That word doesn't exist!")
else:
    print(d[i])

#Alternatively catch the error
try:
    print(d[i])
except KeyError:
    print("That word doesn't exist!")