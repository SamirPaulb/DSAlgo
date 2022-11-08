__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1186/A

Solution: If the minimum of pens and notepads is more than or equal to n, Cossack can reward everyone.
Return the result accordingly. 
'''


def solve(n, m, k):

    return "YES" if min(m, k) >= n else "NO"


if __name__ == "__main__":

    n, m, k = map(int, raw_input().split(" "))
    print solve(n, m, k)
