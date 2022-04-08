from admin_login import admin_login
from user_login import user_login


def choiceAgain(input_choice):
    if input_choice == 1:
        admin_login()
    elif input_choice == 2:
        user_login()
    else:
        print("Enter the valid choice")


def login():
    # ******Welcome to BookMyShow *******
    # User: Admin
    # Password: ** ** ** ** **
    print("******Welcome to BookMyShow*******")
    print("1. Admin login")
    print("2. User login")
    print("3. Previous option")

    input_choice = int(input("Enter your choice"))
    if input_choice == 3:
        return
    choiceAgain(input_choice)


