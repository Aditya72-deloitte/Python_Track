# defining Decorators
def multiplyTwice(function):
    def inner(num1, num2):
        print(num1 * num2)
        return function(num1, num2)

    return inner


# initialising Decorators
@multiplyTwice
def multiply(num1, num2):
    print(num1 * num2)


# Taking input
num1 = int(input("Number 1 : "))
num2 = int(input("Number 2 : "))
multiply(num1, num2)
