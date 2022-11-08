__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/139/A
Solution: The idea is reduce the number of pages as per daily consumption quota. Before proceeding for a day, check
if the remaining pages (for the ith day of the week) will result in > 0. The value of i circulates from 0 to 6. The
corresponding week-day number is 1 to 7, hence the +1 in the end. 
'''

def solve(n, daily):

    i = 0
    while n - daily[i] > 0:

        n -= daily[i]
        i = (i+1) % 7

    return i+1 #+1 since array index start from 0, but the weekday start from 1


if __name__ == "__main__":
    n = int(raw_input())
    daily = map(int,raw_input().split(" "))
    print solve(n, daily)