from _csv import reader


def user_login():
    i = 0
    flag = 0
    print("******Welcome to BookMyShow*******")
    print("Enter your credentials")
    userName = str(input("Enter your User name:  "))
    userPass = str(input("Enter your Password:  "))
    with open('User.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        # Check file as empty
        if header is not None:
            # Iterate over each row after the header in the csv
            for row in csv_reader:
                i = i + 1
                # row variable is a list that represents a row in csv
                if row[0] == userName and row[1] == userPass:
                    insideUserLogin()
                else:
                    flag = flag + 1
    if flag == i:
        print("Wrong Credentials")


def insideUserLogin():
    print("*******Welcome User******")