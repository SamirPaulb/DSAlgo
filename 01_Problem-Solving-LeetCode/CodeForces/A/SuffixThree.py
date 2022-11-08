__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1281/A

Solution: Capture the suffixes of the given string to match with the given possible patterns. Return the 
result language accordingly. 

~ Tidbit ~
Use s[-x:] to obtain the last x characters of the string s. 
'''


def solve(s):

    if s[-2:] == "po":
        return "FILIPINO"
    elif s[-4:] == "desu" or s[-4:] == "masu":
        return "JAPANESE"
    elif s[-5:] == "mnida":
        return "KOREAN"
    else:
        return "NONE"


if __name__ == "__main__":

    t = int(raw_input())

    for _ in xrange(0, t):
        s = raw_input()
        print solve(s)
