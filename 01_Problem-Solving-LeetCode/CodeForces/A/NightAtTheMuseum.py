__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/731/A

Solution: Iterate over the string and for every pair of adjacent characters, check if the forward or backward move
is optimal. For forward, we can take the difference of ascii values of previous and current character. Since we want
to know the moves, we take the difference as absolute. For the backward move, we subtract the forward move from 26, since
we have 26 characters only. Minimum of these moves is added to the total moves. 
In order to take care of the first character's move, we prepend 'a' to the string. 
'''


def solve(str):
    str = 'a' + str
    totalMoves = 0

    for i in xrange(1, len(str)):
        prevChar = str[i-1]
        curChar = str[i]

        forwardMove = abs(ord(prevChar) - ord(curChar))
        backwardMove = 26 - forwardMove

        totalMoves += min(forwardMove, backwardMove)

    return totalMoves



if __name__ == "__main__":
    str = raw_input()
    print solve(str)