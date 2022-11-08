__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1304/A

Solution: Relative speed problem. Find the net distance between them (y-x) and their relative speed (a+b since they
are moving towards each other). Now if they actually meet, their time should be same to reach that point between
x and y. Hence net_distance should be divisible by net_speed and the quotient of it would be the answer. Otherwise,
its -1.  
'''


def solve(x, y, a, b):

    net_distance = y - x
    relative_speed = a + b

    return -1 if net_distance % relative_speed != 0 else net_distance / relative_speed


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        x, y, a, b = map(int, raw_input().split(" "))
        results.append(solve(x, y, a, b))

    for result in results:
        print result
