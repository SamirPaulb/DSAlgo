__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1398/B

Solution: Few things about the game play are evident by the observation:
1) Every player tries to target the largest group of consecutive 1s available. Taking part of it or
avoiding it would result in opponent gaining those points.
2) Every player would avoid targeting group of consecutive 0s available. This is because this firstly
doesn't give that player any points and secondly brings the adjacent 1s groups consecutive helping the
opponent gain those points in the next turn. 

So the strategy is to target the groups of 1s in descending order of their length in the original string.
So we first split the string into these groups, sort them in descending order. Finally we iterate over
this list making jumps of 2 (since Alice and Bob alternate their turns), and add the length of 1s
of the current 1s group to Alice's points. Finally return this sum as the answer.  
'''
import re


def solve(s):

    one_groups = re.split("0+", s) # one or more 0s
    one_groups.sort(reverse=True)

    alice_points = 0
    for i in xrange(0, len(one_groups), 2):
        alice_points += len(one_groups[i])

    return alice_points


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        s = raw_input()
        results.append(solve(s))

    for result in results:
        print result
