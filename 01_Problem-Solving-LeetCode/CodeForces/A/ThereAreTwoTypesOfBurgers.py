__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1207/A

Solution: We make a greedy choice to make the costlier burger first, which means exhaust the buns for it first.
Then we make the other one. TO ease the computation, we can consider the hamburger is always the costlier one
and if not, we can swap the values. Also buns are used in twice number for either burgers, so we divide their
quantity first by 2.  
'''


def solve(b, p, f, h, c):

    b /= 2
    earnings = 0

    # greedy choice to prefer costlier burger to make first
    if h < c:
        # swap
        p, f = f, p
        h, c = c, h

    burger_made = min(b, p)
    b -= burger_made
    p -= burger_made
    earnings += burger_made * h

    burger_made = min(b, f)
    b -= burger_made
    f -= burger_made
    earnings += burger_made * c

    return earnings


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        b, p, f = map(int, raw_input().split(" "))
        h, c = map(int, raw_input().split(" "))
        results.append(solve(b, p, f, h, c))

    for result in results:
        print result
