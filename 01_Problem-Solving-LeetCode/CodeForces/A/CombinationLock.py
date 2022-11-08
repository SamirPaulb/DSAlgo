__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/540/A

Solution: We need to find the distance of each corresponding digit in the original and target
combination. The distance would be abs(original[i] - target[i]). The effective distance considering
both directions would be min(distance, 10 - distance). 
'''


def solve(n, original, target):

    moves = 0
    for i in xrange(0, n):

        distance = abs(int(original[i]) - int(target[i]))
        moves += min(distance, 10 - distance)

    return moves


if __name__ == "__main__":

    n = int(raw_input())
    original = raw_input()
    target = raw_input()
    print solve(n, original, target)
