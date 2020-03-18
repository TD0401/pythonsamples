#filter the checklist to remove the items which are not present in the country file
checklist = ["Portugal","Germany","Munster","Spain"]

country = []
with open("../../../../resources/countries-parsed.txt","r") as file:
    country = file.read().strip("\n")

newCheckList = []
for x in checklist:
    if x in country:
        newCheckList.append(x)
print(newCheckList)