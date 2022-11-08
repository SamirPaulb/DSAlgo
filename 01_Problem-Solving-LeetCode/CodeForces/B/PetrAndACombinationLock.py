__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1097/B

Solution: We enumerate all possible cases of the angles' movements. This can be visualized as a
boolean table where we enumerate the cases of either moving an angle clockwise or anti-clockwise.

Say we add in clockwise and subtract in anti-clockwise, for angles 10, 20, 30, 
we can get the following outcomes:

-10 + -20 + -30
-10 + -20 + 30
-10 + 20 + -30
-10 + 20 + 30
10 + -20 + -30
10 + -20 + 30
10 + 20 + -30
10 + 20 + 30

To simulate this, we construct a bitmask an employ bit shifts to check if the ith bit is set or
not in the current enumeration, and accordingly move the ith angle clockwise or anti-clockwise. 

'''


def solve(n, arr):

    total_cases = 1 << n

    for case in xrange(0, total_cases):

        sum_of_angles = 0
        for bit in xrange(0, n):

            if ((1 << bit) & case) != 0:
                sum_of_angles += arr[bit]
            else:
                sum_of_angles -= arr[bit]

        if sum_of_angles % 360 == 0:
            return "YES"

    return "NO"


if __name__ == "__main__":

    n = int(raw_input())

    arr = list()
    for _ in xrange(0, n):
        a = int(raw_input())
        arr.append(a)

    print solve(n, arr)

