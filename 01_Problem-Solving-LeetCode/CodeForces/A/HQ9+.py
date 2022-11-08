__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/133/A

Solution: Just check if any of the characters in the string is H,Q or 9. + does not print anything. 
'''


def solve(input):
    printableChars = set('HQ9')
    for i in xrange(0, len(input)):
        if input[i] in printableChars:
            return "YES"
    return "NO"


if __name__ == "__main__":
    input = raw_input()
    print solve(input)