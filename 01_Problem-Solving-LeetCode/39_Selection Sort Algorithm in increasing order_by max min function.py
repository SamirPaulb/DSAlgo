a = [2,5,1,0,15,226,23,933,9]

for i in range(len(a)):
    min_val = min(a[i:])
    min_ind = a.index(min_val)
    a[i],a[min_ind] = a[min_ind],a[i]
print(a)
