# Python code to convert dictionary into list of tuples

# Initialization of dictionary
dict = {'HuEx': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}

print("Original Dictionary :" + str(dict))

# Converting into list of tuple
list = [(k, v) for k, v in dict.items()]

# Printing list of tuple
print("Converted into List" + str(list))
