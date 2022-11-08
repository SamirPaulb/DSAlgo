__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1382/A

Solution: if there is a common element between the two arrays, that would be the common sub-sequence needed. To make
things faster, we assume the a is shorter in length than b. We store the elements of the longer array in a set and 
iterate over the shorter one.   
'''


def solve(n, m, a, b):

    if n > m:
        return solve(m, n, b, a)

    b_set = set(b)

    for i in xrange(0, n):

        if a[i] in b_set:
            return "YES\n1 " + str(a[i])

    return "NO"


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n, m = map(int, raw_input().split(" "))
        a = map(int, raw_input().split(" "))
        b = map(int, raw_input().split(" "))
        results.append(solve(n, m, a, b))

    for result in results:
        print result
