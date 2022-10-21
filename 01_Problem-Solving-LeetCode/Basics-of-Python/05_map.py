def square(num):
    return num*num

l = [1, 2, 4]

# Method 1
l2 = []
for item in l:
    l2.append(square(item))
print(l2)

# Method 2
print(list(map(square, l)))