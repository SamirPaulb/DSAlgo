__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1141/B

Solution: The magic of this solution lies in appending the hour-status list to itself. Why? Well that helps to handle 
the status of the last hour of prior day with the next day's hours' statuses. Now the problem becomes finding the longest
length of 1s in the appended bigger list. Find and return the max-len found. 
'''


def solve(n, hourStatuses):

    working = 0
    sleeping = 1
    currMaxLen = 0
    globalMaxLen = 0
    hourStatuses += hourStatuses #append the list to itself

    for hourStatus in hourStatuses:

        if hourStatus is sleeping:
            currMaxLen += 1
        else:
            globalMaxLen = max(globalMaxLen, currMaxLen)
            currMaxLen = 0

    return globalMaxLen


if __name__ == "__main__":
    n = int(raw_input())
    hourStatuses = map(int,raw_input().split(" "))
    print solve(n, hourStatuses)