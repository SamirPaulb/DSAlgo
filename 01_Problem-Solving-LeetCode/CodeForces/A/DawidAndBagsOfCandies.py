__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1230/A

Solution: The cheap solution is to try out all the combinations possible for the two friends when we have 4 candy bags.
So the grouping can either be 2-2 or 1-3. Hence we brute-force to try all combinations in those groupings. 

It would be interesting to extend this question beyond 4 candy bags. 
'''


def solve(a1,a2,a3,a4):

    # Try combinations of 2,2
    if (a1 + a2 == a3 + a4) or (a1 + a3 == a2 + a4) or (a1 + a4 == a2 + a3) or (a2 + a3 == a1 + a4):
        return "YES"

    # Try combinations of 1,3
    elif (a1 + a2 + a3 == a4) or (a2 + a3 + a4 == a1) or (a1 + a3 + a4 == a2) or (a1 + a2 + a4 == a3):
        return "YES"

    else:
        return "NO"


if __name__ == "__main__":
    a1,a2,a3,a4 = map(int,raw_input().split(" "))

    print solve(a1,a2,a3,a4)