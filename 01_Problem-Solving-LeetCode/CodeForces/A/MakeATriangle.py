__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1064/A

Solution: By triangle inequality, the sum of any two sides much be strictly greater than the third side, we check for
that against the the three possible inequalities. If any of those doesn't hold true, we calculate the difference needed
and return it as the answer. Since 1 cm is increased in 1 min, we would need this diff number of minutes to make it a
legit triangle.  
'''


def solve(a, b, c):

    if a + b <= c:
        return c - (a + b) + 1
    elif a + c <= b:
        return b - (a + c) + 1
    elif b + c <= a:
        return a - (b + c) + 1
    else:
        return 0


if __name__ == "__main__":

    a, b, c = map(int, raw_input().split(" "))
    print solve(a, b, c)
