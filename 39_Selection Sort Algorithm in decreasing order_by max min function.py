a = [2,5,1,0,15,226,23,933,9]

for i in range(len(a)):
    max_val = max(a[i:])
    max_ind = a.index(max_val)
    a[i],a[max_ind] = a[max_ind],a[i]

print(a)

    

