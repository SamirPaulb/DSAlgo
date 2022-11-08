__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/43/A

Solution: Simplest of all problems. Hold the goals in a dictionary for counting purposes. Keeping a running variable
for max goals and its associated team. 
'''

if __name__ == "__main__":

    n = int(raw_input())

    goals = {}
    max_goals = 0
    max_goals_team = ""

    for _ in xrange(0, n):
        goal_team = raw_input()

        if goal_team not in goals:
            goals[goal_team] = 1
        goals[goal_team] += 1

        if goals[goal_team] > max_goals:
            max_goals = goals[goal_team]
            max_goals_team = goal_team

    print max_goals_team
