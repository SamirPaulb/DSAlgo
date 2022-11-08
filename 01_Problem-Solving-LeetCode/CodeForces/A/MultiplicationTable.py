__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/577/A

Solution: Since i * j == n, n should be divisible by i and j. Hence if x % i == 0, x/i = j <= n. Hence we validate
this condition of row and column numbers from 1 to n. 
'''


def solve(n, x):

    count = 0
    for i in xrange(1, n+1):

        if x % i == 0 and (x/i) <= n:
            count += 1

    return count


if __name__ == "__main__":

    n, x = map(int, raw_input().split(" "))
    print solve(n, x)
