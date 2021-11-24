nums = [1,2,4,5,34,67,4,8,64,48,90]

evens = list(filter(lambda n: n%2 ==0,nums))

print(nums)

double = list(map(lambda n: 2*n, nums))

print(double)

from functools import reduce

def Add_All(a,b):
    return a+b

sum = reduce(Add_All,nums)

print(sum)
