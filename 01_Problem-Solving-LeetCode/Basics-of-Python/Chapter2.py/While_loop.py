'''

i = 0
while i <= 50:
    print(i)
    i = i + 1



fruit = ["Bannana", "Apple", "Mango", "Guava", "Watermelon","Cherry"]
i = 0
while i <= len(fruit):
    print(fruit[i])
    i = i + 1


fruit = ["Bannana", "Apple", "Mango", "Guava", "Watermelon","Cherry"]
for i in range(0,len(fruit)):
    print(fruit[i])

print("----------------------------------------------------------------------------")

for i in range(0,len(fruit),2):
    print(fruit[i])


fruit = ["Bannana", "Apple", "Mango", "Guava", "Watermelon","Cherry"]
for i in fruit:
    print(i)


i = 0
for i in range(0,10):
    print(i)
    if i ==7:
        break
else:
    print("End of the loop")



# Continue statement

i = 0
for i in range(0,10):
    if i ==6:
        continue   # this will skip 6 and do not print 6 and look for 7 after continue
    print(i)



# pass statement 

print("Samir is a vary good boy")

i = 0
while i <10 :
    pass
print("Samir is a vary good boy")

if i == 12 :
    pass

print ("I am the best")


def run(player):
    pass
print("I live in Siliguri")


'''





