__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/268/A

Solution: There are few things to unravel in this problem. Each team would play two matches, one at its home ground and
other at away ground. Hence, we need to track it via two loops. We would run into the case where we can have the same team
index for home and away, hence we skip that case. Now for a match, we capture the home team's home jersey color (number)
and the away team away jersey color (number). If those are same, the home team would be subjected to wear its away
jersey and that is what we need to count for the result. Hence, we keep a counter for home team's away jersey wearing
occurrences. We count these occurrences and return that answer finally.   
'''


def solve(teamsJerseys):

    homeTeamAwayJerseyCounter = 0
    for homeTeamIdx in xrange(0, len(teamsJerseys)):
        for awayTeamIdx in xrange(0, len(teamsJerseys)):

            # team won't play with itself, so skip
            if homeTeamIdx == awayTeamIdx:
                continue

            homeTeamHomeJersey = teamsJerseys[homeTeamIdx][0]
            awayTeamAwayJersey = teamsJerseys[awayTeamIdx][1]

            if homeTeamHomeJersey == awayTeamAwayJersey:
                # home team will also have to wear away jersey
                homeTeamAwayJerseyCounter += 1

    return homeTeamAwayJerseyCounter


if __name__ == "__main__":

    n = int(raw_input())

    teamsJerseys = list()
    for _ in xrange(0, n):
        h, a = map(int, raw_input().split(" "))
        teamsJerseys.append((h, a))

    print solve(teamsJerseys)
