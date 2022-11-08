__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1196/A

Solution: Tricky puzzle. Needs some work to derive the O(1) formula. Let's do that. Let's say a <= b <= c.
A greedy strategy can be to give a and b to Alice and Bob have the largest pile to divide so that there is hope to 
equalize individual share of candles. 

So Alice has a and Bob has b candies.  

Now the difference of Bob and Alice candies is b-a. Hence we split c into 2 groups, b-a and c - (b-a). The first group
goes to Alice to compensate the disparity caused by first 2 piles.

So Alice has a + (b-a) and Bob has b candies. 

The 2nd group c - (b-a) would be divided into 2 parts and given to both persons. 
There is a chance that this group isn't even, so that extra candy would be thrown away as the question explains. 

So Alice has a + (b-a) + (c - (b-a))/2 and Bob has b + (c - (b-a))/2 candies. 

Let's resolve any of those since they should be equal. Say we do that for Bob: b + (c - (b-a))/2

=> b + (c - b + a)/2
=> (2b + c - b + a)/2
=> (b + c + a)/2
=> (a + b + c)/2

Therefore the answer would always be (a + b + c)/2. The integer division takes care of that extra 1 candy if that 2nd
group of c - (b-a) is odd.   
'''


def solve(a, b, c):

    return (a + b + c)/2


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        a, b, c = map(int, raw_input().split(" "))
        results.append(solve(a, b, c))

    for result in results:
        print result
