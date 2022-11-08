__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/469/A

Solution: Simply add all the indices Little X and Y in a set. The length of the set should be equal to n to make sure
their combined efforts can tackle all n levels of the game.
'''


def solve(n, p_arr, q_arr):

    levels = set()
    levels.update(p_arr)
    levels.update(q_arr)

    return "I become the guy." if len(levels) == n else "Oh, my keyboard!"


if __name__ == "__main__":

    n = int(raw_input())
    p_arr = map(int, raw_input().split(" "))
    q_arr = map(int, raw_input().split(" "))
    print solve(n, p_arr[1:], q_arr[1:]) # excluding p and q from their respective lists
