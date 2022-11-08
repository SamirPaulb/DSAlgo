__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/443/A

Solution: Remove the braces, split by the separators and then add the list of characters to a set. The size of that 
set is the no of distinct characters observed. 
'''


def solve(s):

    s = s[1:-1]
    if s == '':
        return 0
    chars = s.split(", ")
    return len(set(chars))


if __name__ == "__main__":

    s = raw_input()
    print solve(s)
