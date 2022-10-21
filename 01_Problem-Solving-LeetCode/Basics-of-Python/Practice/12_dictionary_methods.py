myDict = {
    "Samir": "He is the king of the world",
     "Marks": "Used in Exam",
     "India": "A country in Asia",
     "Dictionary": {"Paul": "A surname"},
     "Natural Number":[1,2,3,4,5,6,7,8,9,10],
     1:2
}
# print(list(myDict.keys())) # prints the keys of the dictionary
# print(myDict.values())  # prints the values of the keys
# print(myDict.items())   # prints all the contents of the dictionary
# print(myDict) # prints all the contents of the dictionary
updateDict = {
    "Lovish" : "Friends"
}
myDict.update(updateDict)
print(myDict)