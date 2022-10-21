'''
a = 14==7
print(a)
b = 13!=4
print(b)


a = True
b = False
print("The Value of a or b is ",a or b)
print("The value of a and b is ",a and b)
print("The value of not b is ", not b)



a =  224.434
b = int(a)
print(type(b))

a = 28
b = float(a)
print(b)

a  = input("Write your name: \n")
n  = int(input("Write value of n : \n"))
b = 32
# print("Good Morning ",a)
# a = int(a)
# print(type(a))
c = int(a)
p = c+b
t = n % p
print(t)


greetings = "Good Morning, "
name = "Samir Paul"
print(greetings, name)
print(greetings+name)



a = "SamirPaul"
print(a[5])
print(a[-1])
print(a[-9])
print(a[0:5])
print(a[-9:-1])
print(a[:-1])
print(a[0:])
print(a[0:9:2])
print(a[0::2])

a = "SamirPaul"

print(len(a)) # Give the length of a String
print(a.find(a))
print(a.replace("a","s"))
print(a.endswith("l"))
print(a.count("a"))
print(a.capitalize())


w = input("Write your name: \n")
x = input("Write the date: \n")
a = """ Hello <s>,
Congratulation you are selected!
Thanks,
Samir Paul
Date: <d>
"""

a = a.replace("<s>",w)
a = a.replace("<d>",x)
print(a)




# Lists
a = [22,4,35,54,"Samir",24,5,6]
print(a)
print(a[5])
print(a[-4])
a[3] = 25
# a[8] = 55    -->Can not do this
print(a)



friends = ["Samir","Aniket","Raj","Partha","Rohan","Sumit"]
print(friends[0:5])
print(friends[-3:])



l1 =  [12,3,5,6,35,7,34,565,33,3,5465,23]
# l1.sort()
#l1.reverse()
#l1.insert(2,45)
#l1.append(921)
#l1.pop(3)
l1.remove(34)

print(l1)


f1 = input("Enter Fruit 1 name: ")
f2 = input("Enter Fruit 2 name: ")
f3 = input("Enter Fruit 3name: ")
f4 = input("Enter Fruit 4 name: ")
f5 = input("Enter Fruit 5 name: ")
f6 = input("Enter Fruit 6 name: ")
f7 = input("Enter Fruit 7 name: ")
f8 = input("Enter Fruit 8 name: ")

print(f1,f2,f3,f4,f5,f6,f7,f8)


#  ## Dictionary ##

myDict = {
    "Fastly": "Doing thing in a fast manner",
    "Dictionary": "Stock of words with meaning",
    "Samir Paul": "King of the world",
    "AnotherDict": {
        "Paul": "A surname",
        "Proton": "Constituent of matter",
        "Gasoline": "A petrolium fuel"

    },
    1: 22 

}
print(myDict['Fastly'])
print(myDict["Samir Paul"])
print(myDict['AnotherDict']['Gasoline'])
print(myDict['AnotherDict']['Proton'])
print(myDict.keys())
print(myDict.values())
print(myDict.items())
# To update dictionary and add elements
updateDict = {
    "Subham": "A name",
    "Siliguri": "A city in Darjeeling district",
    "Fastly": "in a quick manner"

}
myDict.update(updateDict)
print(myDict)

print(myDict.get('Fast')) # Same value as associeted
print(myDict['Fast'])  # Same value as associeted

print(myDict.get('Fast12')) # Returns None as Fast12 key is not present in the dictionary
print(myDict['Fast12'])  # Key Error as Fast12 key is not present in the dictionary


a = set()
print(type(a))
a.add(2)
a.add(5)
a.add(8)
a.add((5,6,2,9,7,1,0,3))
# a.add({4:5})     Can not be added
print(a)


b = set()
b.add(1)
b.add(2)
b.add(3)
b.add(4)
b.add(5)
b.add(6)
b.add(7)
b.add(8)
b.add(9)
b.add(10)
b.add(11)
b.add(12)
b.add(13)
b.add(14)
b.add(14)
b.add(15)
b.add(5)
b.add(6)
b.add(5)

print(b)
print(b.pop())
b.remove(5)
print(b)


# A dictionary of Hindi Words

myDict = {
    "Pankha": "Fan",
    "Dabba": "Box",
    "Ghar": "House"
}
print("Available words in this dictionary are: ", myDict.keys())
a = input("Write the word you wanna find \n")
print("The meaning of your word ",a," is:  ",myDict[a])  #throw error if does not match
print("The meaning of your word ",a," is:  ",myDict.get(a)) # throw None if not match



s = {21,23,43,12,21,21,2.32,"13","ada",23}
print(s)

s = set()
s.add(12)
s.add(12.32)
s.add("23")
s.add(45)
s.add("Samir")
print(len(s))


a = {23 , 23.00 , 23.0 , 23.000000000}
print(len(a))

b = {}
print(type(b))  # it is a Dictionary





Fav = {}
a = input("Enter you favourit language SAMIR :\n")
b = input("Enter you favourit language RAHUL :\n")
c = input("Enter you favourit language SHOURAV :\n")
d = input("Enter you favourit language PATHIK :\n")
e = input("Enter you favourit language SANDIP :\n")
f = input("Enter you favourit language ANIKET :\n")
g = input("Enter you favourit language HEMACHANDER :\n")

Fav["SAMIR"] = a
Fav["SAMIR"] = b
Fav["SHOURAV"] = c
Fav["PATHIK"] = d
Fav["SANDIP"] = e
Fav["ANIKET"] = f
Fav["HEMACHANDER"] = g
print(Fav)

'''













