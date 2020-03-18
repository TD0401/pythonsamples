#Please concatenate this file with this one to a single text file. The content of the output file should look like below.


import pandas

data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2 = pandas.read_csv("http://pythonhow.com/data/sampledata_x_2.txt")

print(data)
print(data2)

data3 = data.append(data2, ignore_index=True)
data3.to_csv("../../../../resources/sampleConcatenate.txt",index=None)

#Alternatively

data4 = pandas.concat([data,data2])
data4.to_csv("../../../../resources/sampleConcatWoIndex.txt", index=None)

