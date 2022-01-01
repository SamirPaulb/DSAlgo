n = int(input("type the number upto which you wanna find PRIME number:   "))
a = []
if n>1:
    for  i in range(2,n+1):
        for j in range(2,i):
            if i%j ==0:
                break
        else:
            a.append(i)
    print(a)
    
            




