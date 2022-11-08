__author__ = 'deveshbajpai'
'''
Problem Url: http://codeforces.com/problemset/problem/527/A

Algorithm: Very interesting problem. It runs quite parallel to the intuition behind Euclid Algorithm for GCD.
'''


def solve(a,b):

    squares = 0

    while a > 0 and b > 0:

        if a > b:
            squares += a/b
            a %= b
        else:
            squares += b/a
            b %= a

    return squares


if __name__ == "__main__":
    a,b = map(int,raw_input().split(" "))
    print solve(a,b)