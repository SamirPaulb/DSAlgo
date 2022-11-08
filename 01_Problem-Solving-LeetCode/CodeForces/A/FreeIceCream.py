__author__ = 'Devesh Bajpai'

'''
TODO: Not all testcases are passing yet. 
https://codeforces.com/problemset/problem/686/A

Solution: Straightforward. Run through the people in the list. If they are of type delivery (+), increase the count of
ice cream packs. If not, check if there are sufficient packs, if so update the packs after deducting teh person's demand
from it. Else, there aren't enough to be given hence the person is a distressed kid, whose counter should be incremented.
'''


def solve(n, x, people):

    ice_cream_packs = x
    distressed_kids = 0

    for p in people:

        # 0 is type, 1 is quantity
        if p[0] == '+':
            ice_cream_packs += p[1]
        elif p[1] > ice_cream_packs:
            distressed_kids += 1
        else:
            ice_cream_packs -= p[1]

    return str(ice_cream_packs) + " " + str(distressed_kids)


if __name__ == "__main__":

    n, x = map(int, raw_input().split(" "))

    people = list()
    for _ in xrange(0, n):
        type, quantity = raw_input().split(" ")
        people.append([type, int(quantity)])

    print solve(n, x, people)
