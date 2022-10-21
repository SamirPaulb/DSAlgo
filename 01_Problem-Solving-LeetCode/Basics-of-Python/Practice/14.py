
ints = [1, 2, 88, -100, 49]
total = 0
for i in range(len(ints)):
   total = total + ints[i]
   if total < 0:
        break
   print (ints[i])


