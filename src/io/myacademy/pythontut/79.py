#Password checker - contains 1 number, 1 upperCase, 5 char long




password = list(input("Enter a password"))
if(len(password) < 5):
    print("Password is not fine")
strArr =  password
isDigit = False
isUpper = False
for x in password:
    if(str.isdigit(x)):
        isDigit = True
    elif str.isupper(x):
        isUpper = True

if not isDigit or not isUpper:
    print("Password is not fine")
else:
    print("Password is fine")



