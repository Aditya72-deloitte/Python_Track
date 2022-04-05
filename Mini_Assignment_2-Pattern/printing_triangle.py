n = int(input("Enter the height of triangle : "))
n=n*2-1

for i in range (n):
    for j in range (n):
        if(i>(n/2)-1):
            if(not(i-j)):
                print('*', end ="")
            elif(i+j==n-1):
                print('*',end="")
            elif(i==n-1):
                print("*",end="")
            else:
                print(" ",end="")
    if(i>n/2-1):
        print()