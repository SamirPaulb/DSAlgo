# https://codeforces.com/problemset/problem/1539/C

n, k, x = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
# print(arr)
diffArr = []
for i in range(1, len(arr)):
    diff = arr[i] - arr[i-1]
    if diff > x: diffArr.append(diff)

res = 0
diffArr.sort()
# print(diffArr)
for diff in diffArr:
    if diff <= (k+1)*x and k > 0:
        k = k - (diff - 1) // x
    else:
        res += 1

print(res+1)
