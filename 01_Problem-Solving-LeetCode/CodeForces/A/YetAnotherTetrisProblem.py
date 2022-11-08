__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/blog/entry/74714

Solution: Since we add blocks of size 2x1 (without rotation) to the existing columns, 
their parity doesn't change. That is because:
even + odd  = odd
even + even = even  

Hence we need to check that all the elements in the array have the same parity or not, and accordingly
return the result. 
'''


def solve(n, arr):

    parity = arr[0] % 2

    for i in xrange(1, n):
        if arr[i] % 2 != parity:
            return "NO"

    return "YES"


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        arr = map(int, raw_input().split(" "))
        results.append(solve(n, arr))

    for result in results:
        print result
