# Program To Check Entered Number is Prime or Not

n = int(input("input a number to check wheather it is prime or not:  "))
if n>=1:
    if n==1:
        print("1 is NOT PRIME Number")
    else:
        for i in range(2,n):
            if n%i ==0:
                print(f"The number {n} is NOT a PRIME number")
                break
        else:
            print(f"The number {n} is a PRIME number")
else:
    print(f"The number {n} is NOT a PRIME number")


