__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1385/B

Solution: The question boils down to have a linked hash set of the given array. That would preserve unique elements in
the order of their occurrences in the original array. We use OrderedDict for that here. 
'''

from collections import OrderedDict


def solve(arr):

    arr_linked_hash_set = list(OrderedDict.fromkeys(arr).keys())

    return " ".join(str(_) for _ in arr_linked_hash_set)


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        raw_input() # ignoring n
        arr = map(int, raw_input().split(" "))
        results.append(solve(arr))

    for result in results:
        print result
