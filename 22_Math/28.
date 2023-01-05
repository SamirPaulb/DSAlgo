# https://codeforces.com/contest/727/problem/A


# Reverse approach

a,b = map(int, input().split())
arr = []
while b >= a: 
    arr.append(b)
    if b%2 == 0:
        b //= 2
    elif b%10 == 1:
        b -= 1
        b //= 10
    else:
        break

if a in arr:
    print("YES")
    print(len(arr))
    print(*arr[::-1])
else:
    print("NO")
