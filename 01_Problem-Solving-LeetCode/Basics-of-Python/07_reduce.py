from functools import reduce

sum = lambda a, b: a+b

l = [1, 2, 3, 4]
val = reduce(sum, l)
print(val)