__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1368/A

Solution: We simply simulate the operation of += on the given operands. To decide which variable
gets updated, we employ the greedy strategy to update the smaller value. This way, we have a
bigger value to be updated in the next round. e.g.

a = 3, b = 5
We can get:
 a += b, a = 8, b = 5
 or
 b += a, a = 3, b = 8
 
 The first case will lead to b getting updated to 13 in the next round while in the later one
 we can only update a or b to 11.  
'''


def solve(a, b, n):

    operations = 0

    while a <= n and b <= n:

        if a < b:
            a += b
        else:
            b += a

        operations += 1

    return operations


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        a, b, n = map(int, raw_input().split(" "))
        results.append(solve(a, b, n))

    for result in results:
        print result
