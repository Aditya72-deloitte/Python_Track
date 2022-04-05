class StringClass:
    """
    A representation of a person
    Attributes:
        Firstname(string)
        Lastname(String)
    """

    def __init__(self):
        self.firstname = ''

    def getStr(self):
        self.firstname = input('Enter your String : ')

    def show_full_name(self):
        return len(self.firstname)

    # Python3 program to Split string into characters
    def split(self):
        return [char for char in self.firstname]



# creating an object with the class
person2 = StringClass()
person2.getStr()
print(person2.split())
print(person2.show_full_name())