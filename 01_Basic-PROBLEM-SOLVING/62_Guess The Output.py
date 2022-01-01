def function(n,list1 = []):
    list1.append(list1.append(n))
    return list1

for i in range(4):
    list2 = function(i)

print(list2)



# Answer:  [0, None, 1, None, 2, None, 3, None]