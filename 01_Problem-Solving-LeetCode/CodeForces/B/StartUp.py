__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/421/B

Solution: In order for the horizontal reflection to work, the given string should be palindrome and
 each character of the string should be symmetric.  
'''


def solve(s):
    symmetric_letters = {'A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y'}
    n = len(s)

    for i in xrange(0, (n/2)+1):
        left_char = s[i]
        right_char = s[n - i - 1]
        if left_char not in symmetric_letters \
                or right_char not in symmetric_letters \
                or left_char != right_char:
            return "NO"

    return "YES"


if __name__ == "__main__":

    s = raw_input()
    print solve(s)
