__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/701/A

Solution: Convert the given list into a data-structure where each element carries its index and value. Now
sort this data-structure in ascending order of value. Post that, iterate over the it and print the pairs from
both ends. They are bound to have the same sum. 
'''


def solve(n, arr):

    arr_idx = list()

    for i in xrange(0, n):
        arr_idx.append([i+1, arr[i]])

    arr_idx.sort(cmp=custom_compare)

    for i in xrange(0, n/2):
        print str(arr_idx[i][0]) + " " + str(arr_idx[n-i-1][0])


def custom_compare(arr_idx1, arr_idx2):

    return arr_idx1[1] - arr_idx2[1]


if __name__ == "__main__":

    n = int(raw_input())
    arr = map(int, raw_input().split(" "))
    solve(n, arr)
