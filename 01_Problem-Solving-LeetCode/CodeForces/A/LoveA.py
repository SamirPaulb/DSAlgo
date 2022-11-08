__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1146/A

Solution: Say we have a number of 'a's in the given string s. After removal of few characters from
the string s, its length is m. So a/m > 1/2

=> a/m > 1/2
=> 2a/m > 1
=> 2a > m

So it would safe to say, 2a - 1 >= m 
Therefore the final length of string s should be 2a - 1. But we also know it cannot be greater than
len(s) = n as we are only allowed to delete characters, not add them. Hence the answer is 
min(2a - 1, n)
'''


def solve(s):

    a = s.count('a')
    return min(2*a - 1, len(s))


if __name__ == "__main__":

    s = raw_input()
    print solve(s)
