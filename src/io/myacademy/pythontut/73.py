#Create a script that reads this file, multiplies its values by two and saves the output in a new text file.

import pandas


data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data_2 = data *2
data_2.to_csv("../../../../resources/sampledata2.txt",index=None)