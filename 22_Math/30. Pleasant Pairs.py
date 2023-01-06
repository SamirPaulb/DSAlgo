# https://codeforces.com/problemset/problem/1541/B
# https://youtu.be/vHavxvnCxik

'''
If arr[i] * arr[j] == i + j, then i+j is multiple of arr[i] so 
instead of checking all the elements check only for index j for
which i+j is multiple of arr[i]. So start j from arr[i] - i and 
skip j by arr[i].
'''

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0
    for i in range(1, n+1):
        for j in range(arr[i-1]-i, n+1, arr[i-1]):
            if i < j and arr[i-1] * arr[j-1] == i + j:
                res += 1

    print(res)
