__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1366/A

Solution: No matter we take 2 sticks and 1 diamond, or 1 stick and 2 diamonds, we collectively use 3 items
from the pool of sticks and diamonds to make 1 end product. Hence the answer seems to be (a + b)/3. But there
can be constraints to the number of sticks and diamonds available. 
Imagine a scenario of 998 sticks and 1 diamond. We could say (998 + 1)/3 = 333 end products are possible. But
As soon as we use use the 1 diamond for first product, we don't have any more diamonds left to use. Hence the
remaining 998 end products cannot be made. Therefore, the final answer need to take the constraint min(a,b) 
also in consideration. 
'''


def solve(a, b):

    return min(min(a, b), (a + b)/3)


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        a, b = map(int, raw_input().split(" "))
        results.append(solve(a, b))

    for result in results:
        print result
