from math import gcd

a,b = map(int,input().split(' '))

# to be Coprime there must not be any common divisor between any numbers unless 1

if gcd(a,b) == 1:
    print(f"{a} and {b} are Coprime")
else:
    print(f"{a} and {b} are  NOT Coprime")
    

'''
a,b = map(int,input().split(' '))

def computeGCD(a,b):
    if b ==0:
        return a
    else:
        return computeGCD(b, a%b)
if computeGCD(a,b) ==1:
    print(f"{a} and {b} are Coprime")
else:
    print(f"{a} and {b} are  NOT Coprime")

'''