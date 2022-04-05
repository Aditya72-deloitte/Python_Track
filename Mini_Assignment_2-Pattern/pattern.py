n = int(input("Enter the height of triangle : "))

for i in range (n):
    for j in range (n):
        if(not(i-j)):
            print("* ",end="")
        elif(not(i)):
            print("* ",end="")
        elif(j==5-1):
            print("* ",end="")
        else:
            print("  ",end="")
    print()