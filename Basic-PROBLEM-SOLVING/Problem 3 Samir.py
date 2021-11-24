a = input("") # this by default takes value as string

curr  = a[0]
count = 1
maxCount = 1

for i in a[1:]:
    if i == curr: count += 1
    maxCount = max(maxCount, count)

print(maxCount)
