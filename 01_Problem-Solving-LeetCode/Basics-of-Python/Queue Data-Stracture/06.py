n = ["a","b","a","b","a","a"]

l = int(len(n))

for i in range(l-1):
    if n[i] == n[i+1]:
        l1 = n.remove(n[i])
print(l1)

