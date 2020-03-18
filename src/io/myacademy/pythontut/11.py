#create a list [1,2,3,4,5,6,7,8,9,10] dynamically

#Solution
l = range(1,11)
print(list(l))

#Explanation
#range()  is a Python built-in function that generates a range of integers. However, range()  creates a Python range object. To get a real list object you need to use the list() function to convert the range object into a list object.