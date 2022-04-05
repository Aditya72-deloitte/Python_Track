n = int(input("Enter the height of Pattern : "))

for i in range (n):
    for j in range (n):
        if(not(i-j)):
            print("* ",end="")
        elif(not(i)):
            print("* ",end="")
        elif(j==n-1):
            print("* ",end="")
        else:
            print("  ",end="")
    print()