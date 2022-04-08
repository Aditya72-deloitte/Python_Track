from _csv import writer

from addMovie import adding_movie


def RegisterNewUser():
    print("******Create New Account******:  ")
    name = str(input("Enter your name:  "))
    email = str(input("Enter your email:  "))
    phone = str(input("Enter your Phone number:  "))
    age = str(input("Enter your Age:  "))
    password = str(input("Enter your password:  "))

    list = [name,email,phone,age,password]
    # Open our existing CSV file in append mode
    # Create a file object for this file
    with open('User.csv', 'a') as f_object:
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)

        adding_movie(writer_object, list)
        print("User Added")

        # Close the file object
        f_object.close()

