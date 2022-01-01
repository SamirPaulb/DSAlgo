#Program to Print Perfect Numbers in Given Interval

upper = int(input("Type the upper number here:  "))
lower = int(input("Type the lower number here:  "))

print(f"The perfect numbers in range[{lower},{upper}] are : ")

for num in range(lower, upper+1):
    sum = 0
    for j in range(1,num):
        if num%j ==0:
            sum = sum +j
    if sum ==num :
        print(num)
    
