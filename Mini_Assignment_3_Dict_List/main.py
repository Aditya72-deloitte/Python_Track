list = [
    [1,1,3,2],
    [9,8,8,1],
    [0,4,5,0,0,1,4]
    ]

res = {}
res1 = {}
res2 = {}
for i in list[0]:
    res[i] = list[0].count(i);
for i in list[1]:
    res1[i] = list[1].count(i);
for i in list[2]:
    res2[i] = list[2].count(i);

for i in res:
    if(res[i] > 1):
        print(i,"->",res[i])

for i in res1:
    if(res1[i] > 1):
        print(i,"->",res1[i])

for i in res2:
    if(res2[i] > 1):
        print(i,"->",res2[i])