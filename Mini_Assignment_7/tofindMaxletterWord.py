# To open file
# file = open("Text.txt", "w")

try:
    # Opening file
    file = open("text.txt", 'r+')

    # Splitting the word on space
    words = file.read().split()

    # Initialising the variable
    maxLength = 0
    maxLengthWord = ""

    # Looping through each word
    for i in range(len(words)):
        if len(words[i]) > maxLength:
            maxLength = len(words[i])
            maxLengthWord = words[i]
    # Printing the longest word
    print(maxLengthWord, " : This is the longest word with length : ", maxLength)

# Closing the file
finally:
    file.close()
