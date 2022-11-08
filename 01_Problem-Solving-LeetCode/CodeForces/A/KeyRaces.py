__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/835/A

Solution: Brute force. Calculate the total time taken for each player which is s * vi + 2 * ti.
Compare the return the result accordingly. 
'''


def solve(s, v1, v2, t1, t2):

    first_player = s*v1 + 2*t1
    second_player = s*v2 + 2*t2
    return "First" if first_player < second_player else "Second" if first_player > second_player else "Friendship"


if __name__ == "__main__":

    s, v1, v2, t1, t2  = map(int, raw_input().split(" "))
    print solve(s, v1, v2, t1, t2)
