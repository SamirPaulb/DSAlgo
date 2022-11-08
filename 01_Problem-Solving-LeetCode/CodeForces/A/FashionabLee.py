__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1369/A

Solution: Draw the polygons and observe the behavior. If one axis is parallel to X axis, it needs to have one
pair of it. Similarly for Y axis and this shows that the combination of 4 is needed in any such polygon. Hence
the n should be divisible by 4. 
'''


def solve(n):

    return "YES" if n % 4 == 0 else "NO"


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        results.append(solve(n))

    for result in results:
        print result
