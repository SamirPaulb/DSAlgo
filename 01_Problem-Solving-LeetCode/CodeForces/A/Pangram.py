__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/520/A

Solution: Maintain a set of characters seen in the string. In the end, the size of that set should be 26 denoting all
characters were observed at least once in the string. Make sure we add characters in one case in the set to deal with
upper/lower case characters.  
'''


def solve(n, string):

    charSet = set()

    for i in xrange(0, n):
        charSet.add(string[i].lower())

    return "YES" if len(charSet) == 26 else "NO"


if __name__ == "__main__":

   n = int(raw_input())
   string = raw_input()

   print solve(n, string)
