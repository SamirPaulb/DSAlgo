from math import gcd
n = int(input("Coprime of: "))
u = int(input("upper limit =  "))
l = int(input("lower limit =  "))

print(f"All coprimes of {n} are:")
for i in range(l,u+1):
    if gcd(i,n) == 1:
        print(i,end=", ")
