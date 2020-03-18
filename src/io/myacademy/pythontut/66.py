#Create an English to Portuguese translation program.

#The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source.

d = dict(weather = "clima", earth = "terra", rain = "chuva")

#Expected Result
#Enter word: earth
#terra


#Sol
i = input("Enter word: ")
i.strip(" ").strip("\n")
print(d[i])

