__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1391/A

Solution: The interesting bit (pun intended) about this problem is that when 2 numbers are bitwise ORed, the bits set
in either of those numbers are set in the result. That means the result number would be at least as much as the 
larger of those 2 numbers. This leads to a postulate that:

a_i OR a_i+1 OR a_i+2 .... a_k >= max(a_i, a_i+1, ... a_k). Hence any ordering of the array 1 to n would satisfy the
condition mentioned in the question. We just return them in their ascending order for ease of implementation. 
'''


def solve(n):

    return " ".join(str(_) for _ in xrange(1, n+1))


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        results.append(solve(n))

    for result in results:
        print result
