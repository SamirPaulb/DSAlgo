__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/339/B

Solution: Since the movement is only possible in clockwise direction, if we already passed the house were we should've
been, we need to go the full circle (n - house) and then reach house a. If not, we can do it in this circle itself. 
Count the time for each movement and that sum is the final answer. 
'''


def solve(n, m, a_arr):

    house = 1
    time = 0

    for a in a_arr:

        if a < house:
            time += (n - house) + a
        else:
            time += a - house

        house = a

    return time


if __name__ == "__main__":

    n, m = map(int, raw_input().split(" "))
    a_arr = map(int, raw_input().split(" "))
    print solve(n, m, a_arr)

