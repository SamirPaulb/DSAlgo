# Merge Sort Algorithm

a = [1,4,45,66,8,89,54,0,5,6,75,675,7,56]

def mergesort(a, l, r):   # l = left, r = right,  m = middle element
    if l < r:
        m = (l+r)//2
        mergesort(a, l, m)
        mergesort(a, m+1, r)
        merge(a, l, m, r)
    return a

def merge(a, l, m, r):
    i = l
    j = m+1
    b = []
    while i <= m and j <= r:
        if a[i] <= a[j]:
            b.append(a[i])
            i += 1
        else:
            b.append(a[j])
            j += 1

    while i <= m:
        b.append(a[i])
        i += 1
    
    while j <= r:
        b.append(a[j])
        j += 1

    for k in range(l, r+1):
        a[k] = b[0]
        b.pop(0)

    
mergesort(a, 0, len(a)-1)
print(a)


