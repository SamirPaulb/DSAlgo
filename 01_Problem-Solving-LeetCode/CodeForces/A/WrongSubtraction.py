__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/977/A

Solution: Simply perform the actions for zero/non-zero last digit of n for k times. Return the final value of n. 
'''


def solve(n, k):

    for _ in xrange(0, k):

        if n % 10 != 0:
            n -= 1
        else:
            n /= 10

    return n


if __name__ == "__main__":

    n, k = map(int, raw_input().split(" "))
    print solve(n, k)
