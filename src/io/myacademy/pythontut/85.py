#Please download the attached countries-raw.txt file. The file contains the list of country names,
# but it also contains some unnecessary text among the countries.

#Please clean the list with Python by generating a new text file that contains a flawless list of country names
# without any other text or break lines in it. The new file content should look like in the expected output.

country =[]
with open("../../../../resources/countries-raw.txt","r") as file:
    for line in file:
        text = line.strip("\n")
        if len(text) > 1 and text != 'Top of Page':
            country.append(text)

with open("../../../../resources/countries-parsed.txt","w") as file:
    for x in country:
        file.write(x+"\n")



