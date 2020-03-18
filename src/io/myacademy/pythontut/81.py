#Password checker - contains 1 number, 1 upperCase, 5 char long , multiple error responses

usernameList =[]
with open("../../../../resources/users.txt", "r") as file:
    usernameList = (file.read().strip("\n"))
username = input("Enter username")
if username in usernameList:
    print("User already exists")
else:
    password = list(input("Enter a password"))
    isLength = len(password) >= 5
    if not isLength:
        print("Password is less than 5 characters")
    strArr = password
    isDigit = False
    isUpper = False
    for x in password:
        if str.isdigit(x):
            isDigit = True
        elif str.isupper(x):
            isUpper = True

    if not isDigit:
        print("Password doesnt contain a number")
    if not isUpper:
        print("Password doesnt contain a upperCase character")
    if isDigit and isUpper and isLength:
        print("Password is fine")



