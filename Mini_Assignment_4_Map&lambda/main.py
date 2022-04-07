a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))
x = int(input("x : "))

equation = lambda a, b, c, x : print(a * (x*x) + (b * x) + c)

equation(a, b, c, x)