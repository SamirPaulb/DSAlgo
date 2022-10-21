n = ["a","b","a","b","a","a"]
l = len(n)

m = []

i = 0
for i in range(int(l/2)):
    m.append(n[int(l/2) + i])

j = 0
for j in range(int(l/2)):
    m.append(n[j])

print(m)  # ['b', 'a', 'a', 'a', 'b', 'a']

