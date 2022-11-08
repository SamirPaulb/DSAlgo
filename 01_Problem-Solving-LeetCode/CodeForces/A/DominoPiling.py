__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/50/A

Solution: Simply divide the board-area by tile-area. Do integer division to ignore the fractional tiles. 
'''


def solve(m, n):
    tileArea = 2*1
    boardArea = m*n
    return boardArea / tileArea

if __name__ == "__main__":
    m, n = map(int, raw_input().split(" "))
    print solve(m,n)