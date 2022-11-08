__author__ = 'deveshbajpai'
'''
Problem Url: http://codeforces.com/problemset/problem/270/A

Algorithm: We know that the sum of internal angles of a polygon is 180(n-2) where n is no. of sides of it.
So if each angle is a, then the following equation holds true:
n*a = 180(n-2). This solves out to n = 360/(180-a). Now if the RHS of that is an integer, we have a valid polygon.
'''


def solve(angle):

    if 360 % (180 - angle) != 0:
        return "NO"
    else:
        return "YES"


if __name__ == "__main__":
    cases = int(input())
    results = list()
    for case in xrange(0,cases):
        angle = int(input())
        results.append(angle)
    for result in results:
        print solve(result)