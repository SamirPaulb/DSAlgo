__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1283/A

Solution: If the minute value is 0, we need to see the hour difference from 24. Otherwise, the
portion of 24th hour is accredited via the minute value and hence we need to calculate the minute difference
along with the hour difference with 23. Return the hour difference multiplied by 60 and add the
minute difference to it. 
'''


def solve(h, m):

    if m == 0:
        h_diff = 24 - h
        m_diff = 0
    else:
        h_diff = 23 - h
        m_diff = 60 - m

    return (h_diff * 60) + m_diff


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        h, m = map(int, raw_input().split(" "))
        results.append(solve(h, m))

    for result in results:
        print result
