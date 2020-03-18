#Create a function that takes a text file as input and returns the number of words contained in the text file.
# Please take into consideration that some words can be separated by a comma with no space.
# For example "Hi,it's me." would need to be counted as three words.
# For your convenience, you can use the text file in the attachment.


def wordCount(filePath):
    file1 = open(filePath, "r")
    count = 0
    for x in file1:
        count += len(x.replace(",", " ").split(" "))
    file1.close()
    return count


print(wordCount("../../../../resources/words2.txt"))


