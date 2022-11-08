__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/265/A

Solution: We track our movement till there is a valid command and a stone to move to. If the current command is same
as the current stone, we advance the pointer of the string s. The pointer of commands t is advanced anyways. Finally, 
the position of the pointer of string s gives the final location. We do +1 to that in order to convert it into 1-indexed
notation. 
'''


def solve(s, t):

    s_len = len(s)
    t_len = len(t)

    s_idx = t_idx = 0

    while t_idx < t_len and s_idx < s_len:

        curr_stone = s[s_idx]
        curr_move = t[t_idx]

        if curr_move == curr_stone:
            s_idx += 1

        t_idx += 1

    return s_idx + 1 # +1 for 1-indexed answer


if __name__ == "__main__":

    s = list(raw_input())
    t = list(raw_input())
    print solve(s, t)
