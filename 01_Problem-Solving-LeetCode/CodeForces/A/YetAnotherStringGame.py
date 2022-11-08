__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1480/A

Solution: Greedily, make every non-a as a and a as b when its Alice's turn. Similarly change all non-z to z and z to y
in Bob's turn. Make these mutation from left to right so that their objective to making the lexicographically smallest
and largest string is attained respectively. 
'''


def solve(s):

    c_arr = list(s)
    is_alice_turn = True
    for i in xrange(0, len(c_arr)):

        if is_alice_turn:
            if c_arr[i] != 'a':
                c_arr[i] = 'a'
            else:
                c_arr[i] = 'b'
        else:
            if c_arr[i] != 'z':
                c_arr[i] = 'z'
            else:
                c_arr[i] = 'y'

        is_alice_turn = not is_alice_turn

    return "".join(c_arr)


if __name__ == "__main__":

    t = int(raw_input())

    for _ in xrange(0, t):
        s = raw_input()
        print solve(s)
