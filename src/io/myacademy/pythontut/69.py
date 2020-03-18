#Please create an empty file (manually as you normally create Python files) and name it requests.py .
# Make sure the file has that name exactly. Then just paste the following code in the file:
#
#Executing the script will throw an error.
# Please fix something to make the program print out the expected output.
# You should not modify the code itself, but something else.
import requests

r = requests.get("http://www.pythonhow.com")
print(r.text[:100])


#Import statements first look for a local file in the current directory (e.g. requests.py).
# If there is such file it imports that file, and not the actual module.

#Solution
#Rename or delete the file requests.py

