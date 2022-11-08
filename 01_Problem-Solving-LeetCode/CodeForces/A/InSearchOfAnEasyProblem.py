__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1030/A

Solution: Straightforward. Run through the answers and return HARD at the first occurrence of a 1. Default return EASY.
'''


def solve(answers):

    for answer in answers:
        if answer == 1:
            return "HARD"

    return "EASY"



if __name__ == "__main__":
    n = int(raw_input())
    answers = map(int, raw_input().split(" "))
    print solve(answers)