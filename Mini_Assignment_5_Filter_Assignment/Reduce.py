from functools import reduce

#initialising List
list = [2, 4, 5, 9, 15, 4]

#using reduce funcion to compute mutiplication
multiply = reduce(lambda a, b: a * b,  list)

#printing everything
print("List : ", list)
print("Last result : ", multiply)