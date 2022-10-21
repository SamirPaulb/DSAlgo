a = set()
a.add(3)
a.add(4)
a.add(5)
a.add(6)
a.add(10)
# a.add((2,3,4,5,,6,7))  # can not add a tuple to a set
# a.add({2,3,4,5,6,7})   # can not add to a set >> unhasheble
# a.add([1,2,3,4,5,6,7,8]) # can not add
print(a)
