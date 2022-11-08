__author__ = 'deveshbajpai'
'''
Problem Url: http://codeforces.com/problemset/problem/327/A

Algorithm: This problem is similar to Maximum Sub-array sum (Kandane) problem.
'''


def solve(a_list):

    flipping_0_curr = 0
    flipping_0_max = -1
    original_1 = 0

    for a in a_list:
        if a == 1:
            original_1 += 1
            if flipping_0_curr > 0:
                flipping_0_curr -= 1
        else:
            flipping_0_curr += 1
            if flipping_0_curr > flipping_0_max:
                flipping_0_max = flipping_0_curr

    return original_1 + flipping_0_max


if __name__ == "__main__":
    n = int(input())
    a_list = map(int,raw_input().split(" "))
    print solve(a_list)