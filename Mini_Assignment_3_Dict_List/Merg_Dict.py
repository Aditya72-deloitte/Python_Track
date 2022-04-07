def combine(dict1 , dict2):
    return (dict1.update(dict2))

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
print("Dictionary 1 : ",dict1)
print("Dictionary 2 : ",dict2)

combine(dict1 , dict2)
print("Merged Dictionary : ",dict1)