#Please create a script that generates 26 text files named a.txt, b.txt, and so on up to z.txt.
# Each file should contain a letter reflecting its filename.
# So, a.txt will contain letter a, b.txt will contain letter b and so on.

#Sol
import string, os

if not os.path.exists("../../../../resources/letters"):
    os.makedirs("../../../../resources/letters")

for letter in string.ascii_lowercase:
    with open("../../../../resources/letters/" + letter + ".txt", "w") as file:
        file.write(letter)