__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/599/A

Solution: The roads Basically there are 3 alternatives of traveling. 
Option 1: Use the road d1 to go to shop 1, return via it, use d2 to go to shop 2 and return via it to home. 
Option 2: Use the road d1 to go to shop 1, go to shop 2 via d3, and return home via d2.
Option 3: Use the smaller of roads (d1/d2) to visit one shop, use d3 to visit the another shop, return via it to shop one
and go back home. Logically this shouldn't be possible in real world though. 
'''


def solve(d1, d2, d3):

    option1 = 2 * d1 + 2 * d2
    option2 = d1 + d2 + d3
    option3 = 2 * (min(d1, d2) + d3)
    return min(min(option1, option2), option3)


if __name__ == "__main__":

    d1, d2, d3 = map(int, raw_input().split(" "))
    print solve(d1, d2, d3)
