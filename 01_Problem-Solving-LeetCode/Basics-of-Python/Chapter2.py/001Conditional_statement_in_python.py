a = [2,3,4,6,9,23,94,1,353,242,45,24]

b = set()
c = set()


for i in range(0,len(a)):
    if(a[i]>10):
        b.add(a[i])
    else:
        c.add(a[i])

print(b)
print(c)
