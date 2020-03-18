#Print out in each line the sum of homologous items of the two sequences.

a = [1, 2, 3]
b = (4, 5, 6)

for i in range(0,len(a)):
    print(a[i] + b[i])


for i,j in zip(a,b):
    print(i + j)