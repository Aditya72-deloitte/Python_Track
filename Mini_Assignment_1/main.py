from collections import Counter


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
        return self.firstname

    def length(self):
        return len(self.firstname)

    # Python3 program to Split string into characters
    def split(self):
        return [char for char in self.firstname]


class SearchCommonElements:
    def getStr():
        strin2 = input('Enter 2nd String : ')
        return strin2

    def common(str1, str2):
        # convert both strings into counter dictionary
        dict1 = Counter(str1)
        dict2 = Counter(str2)

        # take intersection of these dictionaries
        commonDict = dict1 & dict2

        if len(commonDict) == 0:
            print(-1)
            return

        # get a list of common elements
        commonChars = list(commonDict.elements())

        # sort list in ascending order to print resultant
        # string on alphabetical order
        commonChars = sorted(commonChars)

        # join characters without space to produce
        # resultant string
        return [char for char in ''.join(commonChars)]



# creating an object with the class
person2 = StringClass()
str1 = person2.getStr()
print(person2.split())
print(person2.length())

person1 = SearchCommonElements()
str2 = SearchCommonElements.getStr()
print(SearchCommonElements.common(str1,str2))