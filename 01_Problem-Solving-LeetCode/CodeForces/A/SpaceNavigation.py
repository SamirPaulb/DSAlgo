__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1481/A

Solution: The idea is that you should have enough R and L moves to have destination x co-ordinate. Same goes for destination
y co-ordinate. Make sure the counts are compared to the abs() of the co-ordinate value when they are negative. We leverage
collections.Counter for easy frequency map of moves. We destination is 0,0 we can delete all the moves and we would be
at it. Hence we can avoid checking that condition. 
'''

import collections


def solve(p_x, p_y, s):

    freq_map = collections.Counter(s)

    if p_x > 0:
        if freq_map['R'] < p_x:
            return "NO"
    elif p_x < 0:
        if freq_map['L'] < abs(p_x):
            return "NO"

    if p_y > 0:
        if freq_map['U'] < p_y:
            return "NO"
    elif p_y < 0:
        if freq_map['D'] < abs(p_y):
            return "NO"

    return "YES"


if __name__ == "__main__":

    t = int(raw_input())

    for _ in xrange(0, t):
        p_x, p_y = map(int, raw_input().split(" "))
        s = list(raw_input())
        print solve(p_x, p_y, s)
