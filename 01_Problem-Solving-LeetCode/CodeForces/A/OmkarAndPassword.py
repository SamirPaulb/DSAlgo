__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1392/A

Solution: If there exist at least 2 different numbers in the array, it can always be reduced to 1 since addition of those
distinct numbers can result in another distinct number thereby reducing the array to 1 element. Only if there is only 1
distinct number in the array, it cannot be reduced any further and hence remains as size n. We use a set to determine 
the number of distinct numbers in the given array. 
'''


def solve(n, arr):

    uniqs = set()
    for i in xrange(0, n):
        uniqs.add(arr[i])

    return n if len(uniqs) == 1 else 1


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        arr = map(int, raw_input().split(" "))
        print solve(n, arr)
