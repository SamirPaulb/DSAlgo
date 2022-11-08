__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/746/A

Solution: Sort the list and find the missing indices between consecutive keyboards left. 
'''


def solve(keyboards):

    keyboards.sort()

    stolen = 0

    for i in xrange(1, len(keyboards)):

        if keyboards[i] - keyboards[i-1] > 1:
            stolen += keyboards[i] - keyboards[i-1] - 1

    return stolen


if __name__ == "__main__":
    n = int(raw_input())
    keyboards = map(int, raw_input().split(" "))
    print solve(keyboards)
