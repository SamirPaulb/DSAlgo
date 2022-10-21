# importing sys
import sys
n1 = int(input("Write the  number1: \n"))
n2 = int(input("Write the  number2: \n"))
n3 = int(input("Write the  number3: \n"))
n4 = int(input("Write the  number4: \n"))

a = [n1,n2,n3,n4]

min = (sys.maxsize - 1)   # This is the Maximum value possible for a int value = 2^31 - 1
print(min)
for i in range(0,len(a)):
    if(a[i] < min):
        min = a[i]
print("The min of the list ",a," is:  ",min)

