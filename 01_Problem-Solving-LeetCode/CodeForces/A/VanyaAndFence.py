__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/677/A

Solution: Straightforward. Add 2 for height > h, and 1 for otherwise for widths. 
'''


def solve(n,h,heights):
    width = 0
    for height in heights:
        if height > h:
            width += 2
        else:
            width += 1
    return width

if __name__ == "__main__":
    n,h = map(int, raw_input().split(" "))
    heights = map(int, raw_input().split(" "))
    print solve(n,h,heights)