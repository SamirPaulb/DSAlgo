myDict = {
    "Samir": "He is the king of the world",
     "Marks": "Used in Exam",
     "India": "A country in Asia",
     "Dictionary": {"Paul": "A surname"},
     "Natural Number":[1,2,3,4,5,6,7,8,9,10]
}
# print the value of key word of dictionary
print(myDict["Samir"])
print(myDict["Marks"])
print(myDict["India"])
print(myDict["Dictionary"]["Paul"]) # Nasted Dictionary
print(myDict["Natural Number"])
# Dictionary is mutable--we can change any value in the dictionary
#Changing the value below
myDict["Natural Number"] = ["25,39,40,10,3929"]
print(myDict["Natural Number"])