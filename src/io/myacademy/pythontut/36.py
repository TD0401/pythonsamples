#Please download the words1.txt file from the attachment and then create a Python function that takes a text file as input
# and returns the number of words contained in the text file.



def wordCount(filePath):
    file1 = open(filePath, "r")
    count = 0
    for x in file1:
        count += len(x.split(" "))
    file1.close()
    return count


print(wordCount("../../../../resources/words1.txt"))


