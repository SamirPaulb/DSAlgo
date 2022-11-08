__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1006/A

Solution: Lets formally define the replacement algorithm defined here:

2i - 1  |    2i   |  Outcome
Present | Absent  |   2i - 1
Absent  | Present |   2i - 1
Present | Absent  |   Null
Absent  | Absent  |   2i - 1

So all the 2i-1 elements remain as is, while the 2i elements become 2i-1. In other words, the odd
numbers remain as is, while the even ones reduce by 1. We perform this for all elements in the array
and return the result. 

'''


def solve(n, arr):

    for i in xrange(0, n):

        if arr[i] % 2 == 0:
            arr[i] -= 1

    return " ".join(str(_) for _ in arr)


if __name__ == "__main__":

    n = int(raw_input())
    arr = map(int, raw_input().split(" "))
    print solve(n, arr)
