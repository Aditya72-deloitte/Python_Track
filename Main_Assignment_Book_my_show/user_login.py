def user_login():
    userCredentials = {"Aditya": "Dehradun"}
    print('******Welcome to BookMyShow*******')
    print("Enter your credentials")
    userName = str(input("Enter your User Name:  "))
    userPass = str(input("Enter your Pass Name:  "))
    if userCredentials[userName] == userPass:
        print("******Welcome User******* ")
