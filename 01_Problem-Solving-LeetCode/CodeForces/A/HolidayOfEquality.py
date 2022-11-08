__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/758/A

Solution: Find the max-welfare value in the given welfare list. Now, all the other welfare values have to match up this.
Take the sum of the difference of them with it.
'''


def solve(welfare, n):

    maxWelfare = welfare[0]

    for i in xrange(1, n):
        maxWelfare = max(welfare[i], maxWelfare)

    burlesNeeded = 0
    for i in xrange(0, n):
        burlesNeeded += (maxWelfare - welfare[i])

    return burlesNeeded

if __name__ == "__main__":
    n = int(raw_input())
    welfare = map(int, raw_input().split(" "))

    print solve(welfare, n)