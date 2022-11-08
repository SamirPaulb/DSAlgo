__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1373/B

Solution: Since there are just 2 types of characters in the string, there will be at least one interfacing point of the 
different characters. That would be the starting point for any player to start. But the game would stop when at least
one character type is fully consumed. So the count of zeroes and ones is critical and the minimum of those defines
the number of turns the game would go. Since Alica starts first, she will play the even indexed (starting at 0) turns.
So if the minimum count is even indexed (% 2 == 0), then she will be the last one to play and Bob will lose; otherwise
she loses. Return the result accordingly. 
'''


def solve(s):

    zeroes = ones = 0

    for c in s:

        if c == '0':
            zeroes += 1
        else:
            ones += 1

    min_count = min(zeroes, ones)

    if min_count % 2 == 0:
        return "NET"
    else:
        return "DA"


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        s = raw_input()
        results.append(solve(s))

    for result in results:
        print result
