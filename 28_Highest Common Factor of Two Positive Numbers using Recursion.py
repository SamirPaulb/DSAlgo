def computeGCD(a,b):
    if b ==0:
        return a
    else:
        return computeGCD(b, a%b)

a = int(input("a =  "))
b = int(input("b =  "))

print(computeGCD(a,b))

