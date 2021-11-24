def fact(n):
    if n ==0:
        return 1
    else:
        return n*fact(n-1)
    
n = int(input("Write the number: \n"))
print(f"Factorial of {n} is: {fact(n)}")

