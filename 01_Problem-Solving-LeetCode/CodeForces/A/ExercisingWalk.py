__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1332/A

Solution: Mostly we need to calculate the net distance to move in both dimensions. That should be in the range
[x1, x2] and [y1, y2] respectively. There is a special case when we are required to move positive distance in
each dimension and there in space to move (i.e. x1 == x2 or y1 == y2). Evaluate these conditions and return the
result accordingly.  
'''


def solve(a, b, c, d, x, y, x1, y1, x2, y2):

    if a + b > 0 and x1 == x2:
        return "NO"
    if c + d > 0 and y1 == y2:
        return "NO"

    net_dist_x = x + (b - a)
    net_dist_y = y + (d - c)

    if not net_dist_x >= x1 or not net_dist_x <= x2:
        return "NO"
    if not net_dist_y >= y1 or not net_dist_y <= y2:
        return "NO"

    return "YES"


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        a, b, c, d = map(int, raw_input().split(" "))
        x, y, x1, y1, x2, y2 = map(int, raw_input().split(" "))
        results.append(solve(a, b, c, d, x, y, x1, y1, x2, y2))

    for result in results:
        print result
