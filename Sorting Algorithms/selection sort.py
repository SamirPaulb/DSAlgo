a = [1,4,45,66,8,89,54,0,5,6,75,675,7,56]

for i in range(len(a)-1):
    m = min(a[i+1:])
    mi = a.index(m)
    if m < a[i]:
        a[i], a[mi] = a[mi], a[i]

print(a)
