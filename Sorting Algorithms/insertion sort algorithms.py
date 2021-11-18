'''
a = [1,4,45,66,8,89,54,0,5,6,75,675,7,56]

for i in range(1,len(a)):
    for j in range(i):
        if a[j] > a[i]:
            a.insert(j, a[i])
            a.pop(i+1)
            break
print(a)

'''
# INSERTION SORT Algorithm

a = [1,4,45,66,8,89,54,0,5,6,75,675,7,56]

def insertionsort(a):
    for i in range(1, len(a)):
        currrent_element = a[i]
        position = i
        while currrent_element < a[position-1] and position > 0:
            a[position] = a[position-1]
            position -= 1
        a[position] = currrent_element
    return a

insertionsort(a)
print(a)

            