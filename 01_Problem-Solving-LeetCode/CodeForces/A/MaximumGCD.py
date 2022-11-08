__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1370/A

Solution: GCD gives the biggest divisor for the given numbers. For a given number, we can go till its half to get the 
biggest factor. Therefore, if n is even, n/2 should give the other number which would be the GCD. Otherwise whe n is 
odd, n-1 would be even and we can follow the above logic. Since integer division ignores the fractional part, n/2 works 
for both cases. 
'''


def solve(n):

    return n/2


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        results.append(solve(n))

    for result in results:
        print result
