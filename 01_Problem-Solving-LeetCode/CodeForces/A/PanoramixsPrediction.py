__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/80/A

Solution: The idea is to check numbers in the range [n+1, m) if anyone of them is prime or not. If so, then surely m
is not the next prime number. If that range doesn't find a prime number, we need to check if m itself is prime or not.
Accordingly, we return the result.  

Improvement: We can surely use Sieve of Eratosthenes for a better way to figure out if a number is prime or not.
'''

import math


def is_prime(x):

    for i in xrange(2, int(math.sqrt(x))+1):

        if x % i == 0:
            return False

    return True


def solve(n, m):

    for i in xrange(n+1, m):

        if is_prime(i):
            return "NO"

    return "YES" if is_prime(m) else "NO"


if __name__ == "__main__":

    n,m = map(int, raw_input().split(" "))
    print solve(n, m)