d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
n = input()    # CMXCVIII = 998
ans = d[n[0]]
for i in range(1,len(n)):
    if d[n[i-1]] < d[n[i]]:
        ans += d[n[i]] - d[n[i-1]]*2
    else:
        ans += d[n[i]]

print(ans)
