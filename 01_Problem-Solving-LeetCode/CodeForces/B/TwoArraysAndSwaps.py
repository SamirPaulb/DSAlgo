__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1353/B

Solution: The idea is sort the array a in ascending order, while array b in descending. Now if we iterate from index 0,
we encounter the smallest numbers in array a which encountering biggest ones in b. So those can be the candidates to be
swapped and hence we sum the max of those two values as we iterate. This is done for k times since we cannot swap more
than k pairs. Post this, we just sum the values from array a from index k to n-1. 
'''


def solve(n, k, arr_a, arr_b):

    arr_a.sort()
    arr_b.sort(reverse=True)

    sum = 0
    for i in xrange(0, k):

        sum += max(arr_a[i], arr_b[i])

    for i in xrange(k, n):

        sum += arr_a[i]

    return sum


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):

        n, k = map(int, raw_input().split(" "))
        arr_a = map(int, raw_input().split(" "))
        arr_b = map(int, raw_input().split(" "))

        results.append(solve(n, k, arr_a, arr_b))

    for result in results:
        print result
