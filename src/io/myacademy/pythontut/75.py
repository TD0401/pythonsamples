#plot the data in the sampleData.txt file
import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data.plot(x='x', y='y', kind='scatter')
plt.show()