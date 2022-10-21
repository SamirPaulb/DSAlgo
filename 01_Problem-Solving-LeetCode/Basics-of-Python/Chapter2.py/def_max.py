'''
def maximum(n1,n2,n3):
    if(n1>n2):
        if(n1>n3):
            return n1
        else:
            return n3
    else:
        if(n2>n3):
            return n2
        else:
            return n3

print(maximum(2,4,6))

'''
'''
a = [4,235,-1501]

if(a[0]>a[1]):
    if(a[0]>a[2]):
        print(a[0]) 
    else:
        print(a[2])
else:
    if(a[1]>a[2]):
        print(a[1])
    else:
        print(a[2])

'''

'''

import sys
a = [2,4,6,7,90,0,45466,32235,542,-534]
max = -(sys.maxsize-1)
print(min)
for i in range(len(a)):
    if a[i]>max:
        max = a[i]

print(max)

'''







