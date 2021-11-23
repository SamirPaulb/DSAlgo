for i in range(1001):
    num = i
    result = 0
    n = len(str(i))
    while (i !=0):
        digit = i%10
        result = result + digit**n
        i = i//10
    if num == result:
        print(result)
    

'''

n = int(input("Enter upto which digit you want to find Angstrom number:  "))

for i in range(1,n+1):
    l = len(str(i))
    result = 0
    a = str(i)
    for j in range(l):
        result = result + int(a[j])**l
    if result == i:
        print(i)
    

'''

