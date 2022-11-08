__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1516/A

Solution: Iterate over the array and reduce the elements left to right and
increase the last element in every move. This ensures that we generate the 
lexicographically smallest array. In order to not let an array element go 
negative, we move the index rightwards when an element is already 0 or negative.
'''


def solve(n, k, arr):

    i = 0
    while k > 0 and i < n:

        if arr[i] <= 0:
            i += 1
            continue

        arr[i] -= 1
        arr[n-1] += 1
        k -= 1

    return " ".join(str(_) for _ in arr)


if __name__ == "__main__":

    t = int(raw_input())

    for _ in xrange(0, t):
        n, k = map(int, raw_input().split(" "))
        arr = map(int, raw_input().split(" "))
        print solve(n, k, arr)
