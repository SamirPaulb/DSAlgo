n = int(input("Write a number to get factorial of that number: \n"))
if n>0:
    factorial = n
    for i in range(1,n):
        factorial = factorial*(n-i)
    print(factorial)
else:
    print("Type only Whole number")
    

