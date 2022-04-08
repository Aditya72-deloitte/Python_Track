import csv

with open("User.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[1])
