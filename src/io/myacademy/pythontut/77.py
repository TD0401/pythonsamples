#Create a script that asks the user to enter their age and the script calculates the user's year of birth
# and prints it out in a string like in the expected output. Please make sure you generate the current year dynamically.

import datetime

age = int(input("Enter your age"))
year = datetime.datetime.now().year.__sub__(age)
print(year)
