import uuid

with open("../../../../resources/uuid.txt", "r") as file:
    for x in file:
        try:
            uuid.UUID(x)
        except:
            print(x)
