from functools import reduce

nums = [1,2,4,5,34,67,4,8,64,48,90]

sum = reduce(lambda a,b: a+b,nums)

print(sum)
