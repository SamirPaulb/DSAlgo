# Write a programme to check zero is present in a given number

n = int(input("Write the number here: \n"))
while n !=0:
    if n%10 ==0:
        break
    n = int(n/10)
if n%10 ==0:
    print("The number has zero in it")
else:
    print("The Number has NOT zero in it")
