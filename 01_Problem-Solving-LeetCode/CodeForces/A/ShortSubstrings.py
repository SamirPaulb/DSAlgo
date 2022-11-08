__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1367/A

Solution: Capture the alternate characters of b to form a. If the length of b is even, we would miss the
last character, hence add it separately. 
'''


def solve(b):

    a = list()

    l = len(b)
    for i in xrange(0, l, 2):
        a.append(b[i])

    # append the last character if the length of b is even, it would be missed up the above loop
    if l % 2 == 0:
        a.append(b[-1])

    return "".join(a)


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        b = raw_input()
        results.append(solve(b))

    for result in results:
        print result
