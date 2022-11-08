__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/999/A

Solution: Iterate from both ends (one at a time) and track how far can we go till the corresponding
value is <= k. Using how far we go, we can calculate the problems Mishka solved in total. 
'''


def solve(n, k, arr):

    i = 0
    while i < n and arr[i] <= k:
        i += 1

    j = n-1
    while j > i and arr[j] <= k:
        j -= 1

    return i + (n - j) - 1


if __name__ == "__main__":

    n, k = map(int, raw_input().split(" "))
    arr = map(int, raw_input().split(" "))
    print solve(n, k, arr)
