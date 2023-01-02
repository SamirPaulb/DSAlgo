'''
https://codeforces.com/problemset/problem/1360/C

Solution: We first count the number of evens and odds in the array. If both these counts are 
not having the same parity, then there isn't a way to partition the array into similar pairs. If
they are, we first check if both counts are even. This makes it possible to divide the even numbers
together, and odd numbers together in similar pairs. If these counts are odd, we would have a pair
of even and odd number. The only way to make their pair similar is to check they are consecutive 
(|a-b| = 1). Easy way to find that is to sort the array and check the conscutive elements. Return
the result accordingly.   
'''


def solve(n, arr):

    even = odd = 0
    for a in arr:
        if a % 2 == 0: even += 1
        else: odd += 1

    if even % 2 != odd % 2: return "NO"
    elif even % 2 == 0: return "YES"
    else:
        arr.sort()
        for i in range(1, n):
            if arr[i] - arr[i-1] == 1:
                return "YES"
        return "NO"




if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        arr = list(map(int, input().split(" ")))
        print(solve(n, arr))
