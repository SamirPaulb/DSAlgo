__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1358/B

Solution: Carefully observing the question, we can see that we don't need to summon the grannies
in batches, rather can do them all at once as long as their constraint of enough grannies present
in the courtyard is satisfied. This would produce the same result as summoning them in batches as
explained in the question. We sort the array and iterate in descending order. This way, for any
value which is less that or equal to its index (+1 since question works on 1 - indexed), that is the
breakage point and all the grannies before that can be summoned. The result returned is i + 2, 
since i + 1 takes care of 1-indexed quantities of grannies and that extra one is for the host. 
Also arr[i] <= (i + 1) can be understood as ith granny needing i + 1 grannies in the yard, which 
excludes herself but can include the host, therefore i + 1 - 1 + 1 = i + 1.
'''


def solve(n, arr):

    arr.sort()

    for i in xrange(n-1, -1, -1):

        if arr[i] <= (i + 1):
            return i + 2

    return 1


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        arr = map(int, raw_input().split(" "))
        results.append(solve(n, arr))

    for result in results:
        print result
