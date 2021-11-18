# Find first 3 nearest points from a[0]
Matrix = [[0,0,0], [4,5,6], [2, 8, 2], [1,6,2], [42,24,1], [13,0, 1]]

dic = {}

for i in Matrix[1:]:
    # distance = x + y + z
    if len(dic) <= 3: dic[sum(i)] = i
    else:
        maxDis = max(dic.keys())
        if sum(i) < maxDis:
            del dic[maxDis]
            dic[sum(i)] = i

for i in range(3):
    m = min(dic.keys())
    print(dic[m])
    del dic[m]


