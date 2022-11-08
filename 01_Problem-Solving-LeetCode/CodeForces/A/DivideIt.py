__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1176/A

Solution: When n is divisible by 2, we do one operation of n/2. When it is divisible by 3, even though we do one operation
of 2n/3, the 2 multiplied in the numerator will cause one operation of n/2. Hence it amounts to two operations. Similarly,
4n/5 amounts to one n/5 and two n/2 operations, totalling to three operations. We proceed the divisions and counting the
operations till n is reduced to 1. At any point if n is not divisible by either 2,3 or 5, we return -1. Finally the 
count in operations is returned as the final answer. 
'''


def solve(n):

    operations = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
            operations += 1
        elif n % 3 == 0:
            n /= 3
            operations += 2
        elif n % 5 == 0:
            n /= 5
            operations += 3
        else:
            return -1

    return operations


if __name__ == "__main__":

    t = int(raw_input())

    for _ in xrange(0, t):
        n = int(raw_input())
        print solve(n)
