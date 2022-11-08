__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1335/A

Solution: Splitting a number n as a sum of two numbers will have a property that after its half, the values a and b
get swapped. e.g.

7 = 1 + 6
7 = 2 + 5
7 = 3 + 4

After that

7 = 4 + 3
7 = 5 + 2
7 = 6 + 1

Therefore, we only need to consider on set of those sums which means we would have (n-1)/2 combinations. The n-1 takes
care of avoiding the equality case when n is even, since the sisters cannot have equal number of candies. 
'''


def solve(n):

    return (n - 1)/2


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        results.append(solve(n))

    for result in results:
        print result
