__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/802/G

Solution: Iterate over the given s while also over the target string which here is "heidi". If the
former's current character is same as that of later, then move the target string's index. In the end
the target string's index should be equal to target's length. If it is, return YES, else NO. 
'''


def solve(s):

    target = "heidi"
    j = 0
    t_len = len(target)
    s_len = len(s)
    for i in xrange(0, s_len):
        if s[i] == target[j]:
            j += 1
            if j == t_len:
                break

    return "YES" if j == t_len else "NO"


if __name__ == "__main__":

    s = raw_input()
    print solve(s)
