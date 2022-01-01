a = [2,5,1,0,15,226,23,933,9,0,2,15324,2,15]

# In decreasing order

for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i] <a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print(a)
