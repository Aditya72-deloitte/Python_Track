list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list2 = ["h", "i", "j"]

print("List : ",list1)
print("SubList : ",list2)

for i in range (0,len(list2)):
    (list1[2][1][2]).append(list2[i])

print("Updated List : ", list1)