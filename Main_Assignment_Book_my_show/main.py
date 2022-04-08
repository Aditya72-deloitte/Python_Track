from RegisterNewUser import RegisterNewUser
from login import login


def numbers_to_strings(choice):
    if choice == '1':
        login()
    elif choice == '2':
        RegisterNewUser()
    else:
        print("Enter valid Choice")


while True:
    print('******Welcome to BookMyShow*******')
    print('1. Login')
    print('2. Register new user')
    print('3. Exit')

    choice = int(input("Enter your option: "))
    if choice == 3:
        exit()
    numbers_to_strings(str(choice))
