__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/448/A

Solution: Straightforward. Sum the cups and the quotient of that with 5 gives the total number of full-filled cups
rows. For the row having not full 5 cups, check for divisibility against 5 and 1 if not. Similarly deal the medals.
The sum of cups and medals needed should be less than or equal to n. 
'''


def solve(n, cups, medals):

    cupsSum = sum(cups)
    cupShelvesNeeded = cupsSum / 5

    if cupsSum % 5 != 0:
        cupShelvesNeeded += 1

    medalsSum = sum(medals)
    medalShelvesNeeded = medalsSum / 10

    if medalsSum % 10 != 0:
        medalShelvesNeeded += 1

    return "YES" if (cupShelvesNeeded + medalShelvesNeeded) <= n else "NO"


if __name__ == "__main__":
    cups = map(int, raw_input().split(" "))
    medals = map(int, raw_input().split(" "))
    n = int(raw_input())
    print solve(n,cups,medals)