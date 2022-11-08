__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/588/A

Solution: A greedy approach can give a good solution to it. We would always want to buy at the cheapest rate so far. 
Hence we keep track of that as we go through the list of quantities (a) and rates (p). The current quantity is multiplied
with that rate and added to the total. 

Time Complexity: O(n) 
'''


def solve(a, p, n):

    if len(a) == 0:
        return 0

    minRateSoFar = p[0]
    total = p[0] * a[0]

    for i in xrange(1, n):

        minRateSoFar = min(minRateSoFar, p[i])
        total += minRateSoFar * a[i]

    return total

if __name__ == "__main__":
    n = int(raw_input())
    a = []
    p = []
    for i in xrange(0,n):
        a_i, p_i = map(int, raw_input().split(" "))
        a.append(a_i)
        p.append(p_i)
    print solve(a, p, n)