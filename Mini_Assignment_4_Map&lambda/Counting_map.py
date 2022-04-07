
#Initialisation of The variable
list1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

#to count the letters on each item
count_a = list(map(lambda x: x.count("a"), list1))
count_A = list(map(lambda x: x.count("A"), list1))

#printing
print("List : ", list1)
print("Count list of 'a' : ", count_a)
print("Count list of 'A' : ", count_A)