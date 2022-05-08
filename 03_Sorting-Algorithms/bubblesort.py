# Bubble Sort Algorithm

a = [12,34,56,8,45,8,3,7,23,7,975,345,7,5,43]

for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]


print(len(a))
