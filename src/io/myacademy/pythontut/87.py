#add missing countries
checklist = ["Portugal","Germany","Spain"]

country = []
with open("../../../../resources/countries-missing.txt","r") as file:
    for line in file:
        country.append(line)

for x in checklist:
    country.append(x+"\n")

country.sort()
with open("../../../../resources/countries-added.txt","w") as file:
    for x in country:
        file.write(x)

