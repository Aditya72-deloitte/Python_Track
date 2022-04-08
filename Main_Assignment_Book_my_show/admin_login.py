from addMovie import addMovie
from deleteMovie import deleteMovie
from editMove import editMovie
from csv import reader


def admin_login():
    i = 0
    flag = 0
    print("******Welcome to BookMyShow*******")
    print("Enter your credentials")
    adminName = str(input("Enter your User name:  "))
    adminPass = str(input("Enter your Password:  "))
    with open('adminCredentials.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        # Check file as empty
        if header is not None:
            # Iterate over each row after the header in the csv
            for row in csv_reader:
                i = i + 1
                # row variable is a list that represents a row in csv
                if row[0] == adminName and row[1] == adminPass:
                    insideAdminLogin()
                else:
                    flag = flag + 1
    if flag == i:
        print("Wrong Credentials")


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
