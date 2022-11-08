__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1003/A

Solution: Since we cannot put the coins of same value in the same pocket, the deterministic factor is the frequency of
the coins of a value. The maximum of that determines the pockets needed. 
'''


def solve(arr):

    freq_map = {}

    for a in arr:
        if a in freq_map:
            freq_map[a] += 1
        else:
            freq_map[a] = 1

    max_freq = 0
    for a in freq_map:
        max_freq = max(freq_map[a], max_freq)

    return max_freq


if __name__ == "__main__":

    raw_input() # ignoring n
    arr = map(int, raw_input().split(" "))
    print solve(arr)
