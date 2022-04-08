# Import writer class from csv module
from csv import writer


def addMovie():
    print("******Welcome Admin*******")
    # creating an empty list
    lst = []

    # number of elements as input
    n = 13

    ele = str(input("Enter title:  "))
    lst.append(ele)  # adding the element
    ele = str(input("Enter genre:  "))
    lst.append(ele)
    ele = str(input("Enter length of Movie:  "))
    lst.append(ele)
    ele = str(input("Enter cast Name:  "))
    lst.append(ele)
    ele = str(input("Enter Director Name:  "))
    lst.append(ele)
    ele = str(input("Enter Admin Rating:  "))
    lst.append(ele)
    ele = str(input("Enter a movie Language:  "))
    lst.append(ele)
    ele = str(input("Enter movie Timing:  "))
    lst.append(ele)
    ele = str(input("Enter First show:  "))
    lst.append(ele)
    ele = str(input("Enter interval time:  "))
    lst.append(ele)
    ele = str(input("Enter gap between shows:  "))
    lst.append(ele)
    ele = str(input("Enter the capacity:  "))
    lst.append(ele)

    # Open our existing CSV file in append mode
    # Create a file object for this file
    with open('MovieList.csv', 'a', newline='') as f_object:
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)

        adding(writer_object, lst)
        print("Movie Added")

        # Close the file object
        f_object.close()


def adding(writer_object, lst):
    # Pass the list as an argument into
    # the writerow()
    writer_object.writerow(lst)

