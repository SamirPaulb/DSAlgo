__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/122/A

Solution: Have a helper method to check if a number is lucky - check all its digits to be 4 or 7
Now for the almost-lucky number check, we need to check its divisors to be lucky. If none found, we return No. 
'''


def solve(n):

    if isLucky(n):
        return "YES"

    for x in xrange(2,n/2):
        if n % x == 0 and (isLucky(x) or isLucky(n/x)):
            return "YES"

    return "NO"


def isLucky(n):

    while n > 0:
        digit = n % 10
        if digit != 4 and digit != 7:
            return False
        n /= 10

    return True


if __name__ == "__main__":
    n = int(raw_input())
    print solve(n)