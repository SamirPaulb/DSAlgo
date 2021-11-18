#Palindromic Prime Numbers
n = input("Write a number:  ")

rev = n[::-1]
if int(n)>1:
    if n == rev:
        for i in range(2,int(n)):
            if int(n)%i ==0:
                print(f"The number {n} is Palindrom but not Prime!")
                break
        else:
            print(f"The Number {n} is both Palindrom and Prime Number.")
    else:
        for i in range(2,int(n)):
            if (int(n)%i) ==0:
                print(f"The Number {n} is Neither Prime Nor Palindrom!")
                break
        else:
            print(f"The Number {n} is only Prime but not Palindrom!")
elif int(n) == 1:
    print("1 is only Palindrom but not prime number!")
    




# Note:  Negetive Numbers are not Palindromic 
