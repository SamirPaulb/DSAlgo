__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1334/A

Solution: Its easy to deduce that even for one player, it is impossible to clear more levels than the plays done. This
also is true when multiple players are there. Secondly, the number of plays or levels cleared cannot go done as they are
non decreasing sequences. Incorporating these 2 conditions, we can check each testcase and evaluate its validity. 
'''


def solve(all_p_c):

    prev_p = prev_c = 0

    for this_p_c in all_p_c:

        delta_p = this_p_c[0] - prev_p
        delta_c = this_p_c[1] - prev_c
        if delta_p < 0 or delta_c < 0 or delta_p < delta_c:
            return "NO"
        prev_p = this_p_c[0]
        prev_c = this_p_c[1]

    return "YES"


if __name__ == "__main__":

    t = int(raw_input())

    for _ in xrange(0, t):
        n = int(raw_input())
        all_p_c = list()
        for _n in xrange(0, n):
            p_c = map(int, raw_input().split(" "))
            all_p_c.append(p_c)
        print solve(all_p_c)
