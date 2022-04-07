sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

print("Before change : ",sampleDict)

#Adding a Location key with the value of city
sampleDict["location"]= sampleDict["city"]

#deleting the City key and value
del sampleDict["city"]

print("New Dict : ",sampleDict)