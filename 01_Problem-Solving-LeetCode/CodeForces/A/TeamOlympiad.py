__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/490/A

Solution: First we segregate the children status into their respective buckets. Then we calculate the lengths of each
bucket and choose the minimum, which is the maximum no. of teams possible since we need a member from each category.
Then we just run a loop for 0 to this size, and pick the the elements from each of those buckets forming teams. 
'''


def solve(n, childrenStatuses):

    programmingLocs = list()
    mathsLocs = list()
    sportsLocs = list()

    for i in xrange(0, n):

        childrenStatus = childrenStatuses[i]

        if childrenStatus == 1:
            programmingLocs.append(i)
        elif childrenStatus == 2:
            mathsLocs.append(i)
        else:
            sportsLocs.append(i)

    maxTeamCountPossible = min(
        len(programmingLocs),
        len(mathsLocs),
        len(sportsLocs))

    teams = list()

    for i in xrange(0, maxTeamCountPossible):

        team = list()

        team.append(programmingLocs[i]+1)  #using location + 1 since the question requires indexing based on 1, not 0.
        team.append(mathsLocs[i]+1)
        team.append(sportsLocs[i]+1)

        teams.append(team)

    return teams


if __name__ == "__main__":

    n = int(raw_input())
    childrenStatuses = map(int,raw_input().split(" "))
    teams = solve(n, childrenStatuses)

    print len(teams)
    for team in teams:
        for t in team:
            print t, #this prints elements in same line separated by space
        print
