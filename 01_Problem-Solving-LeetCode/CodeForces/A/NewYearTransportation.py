__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/500/A

Solution: The idea of this question is same as array hopper problem. Hence we start from the first cell and hop
to the next cell using the hop count from the current cell's value. Also take care if we have gone beyond the 
destination, if so we exit from the loop. This is done since we cannot move backwards. 
'''


def solve(n, dest, portals):

    i = 0
    while i < n:

        if i+1 == dest: # i+1 since the destination is 1 indexed instead of 0
            return "YES"
        elif i+1 > dest: # early exit since portals don't work in backwards direction
            return "NO"
        else:
            i += portals[i]

    return "NO"


if __name__ == "__main__":

    n, dest = map(int, raw_input().split(" "))
    portals = map(int, raw_input().split(" "))
    print solve(n, dest, portals)
