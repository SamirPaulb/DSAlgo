__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1409/A

Solution: Since we can use all numbers from 1 to 10, we try greedily to employ 10 to either increase or decrease a so
that we get a and b only differ in units place. Now for that, we do one another move using the suitable number from 1
to 9. Hence effectively we need to find the difference between a and b first. Then we need to obtain ceil(diff/10). The
ceil takes care of that one extra move using 1 to 9 digits. We employ the equivalent formula for ceil here.  
'''


def solve(a, b):

    return (abs(a - b) + 10 - 1) / 10


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        a, b = map(int, raw_input().split(" "))
        results.append(solve(a, b))

    for result in results:
        print result

