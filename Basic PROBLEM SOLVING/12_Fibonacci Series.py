# Fibonacci Series 0,1,1,2,3,5,8,13,21,34

n = int(input("Type how many numbers your want :  "))
first = 0 
second = 1

for i in range(n):
    print(first)
    temp = first
    first  = second
    second = temp+second



