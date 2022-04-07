#initialisation
list1 = [-1000, 500, -600, 700, 5000, -90000, -17500]

#filtering negative number in res variable
res = list(filter(lambda x: x < 0, list1))

#Changing into same list
for i in range(len(res)):
    res[i] = abs(res[i])

#Printing everything
print("Original List : ", list1)
print("List of negative numbers converted to positive : ", res)