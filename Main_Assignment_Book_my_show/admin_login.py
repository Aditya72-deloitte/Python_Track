from addMovie import addMovie
from deleteMovie import deleteMovie
from editMove import editMovie


def admin_login():
    adminCredentials = {"Admin": "Password"}
    print("******Welcome to BookMyShow*******")
    print("Enter your credentials")
    adminName = str(input("Enter your User name:  "))
    adminPass = str(input("Enter your Password:  "))
    # if adminCredentials[adminName] == adminPass:
    if (adminCredentials.__contains__(adminName)) and (adminPass in adminCredentials.values()):
        insideAdminLogin()
    else:
        print("Try Entering Correct Credentials")


def insideAdminLogin():
    while True:
        print("******Welcome Admin*******")
        print("1. Add new Movie Info")
        print("2. Edit Movie Info")
        print("3. Delete Movie")
        print("4. Logout")
        choice = int(input("Enter your choice"))
        if choice == 4:
            return 0
        elif choice == 1:
            addMovie()
        elif choice == 2:
            editMovie()
        elif choice == 3:
            deleteMovie()
        else:
            print("Enter Valid Choice")
