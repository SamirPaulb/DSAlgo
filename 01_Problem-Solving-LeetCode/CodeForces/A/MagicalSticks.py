__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1371/A

Solution: The test-cases can be divided into 2 categories, when n is even or odd.

When n is even, the approach is straightforward. Just make pairs from 2 ends of the list 1,2,....n 
e.g. n = 4
1, 2, 3, 4

Pairs: (1,4), (2,3)
Hence the formula n/2 makes sense. 

When n is odd, an optimal approach would be to leave the nth stick, and make pairs for the remaining from 2 ends of 
the list (like we did for even cases as n-1 would make it even)
e.g. n = 9
1, 2, 3, 4, 5, 6, 7, 8, 9

Pairs: (1,8), (2,7), (3,6), (4,5)
Solo: 9

Hence the formula (n-1)/2 + 1 makes sense.
Simplifying that, we get (n+1)/2. 

Now we could make an if check for n oddity and use n/2 or (n+1)/2, but the later gives the right answer for even cases
too. That is because when n is even, the answer doesn't consider the fractional quotient and hence we can use this 
formula for both cases. 

'''


def solve(n):

    return (n + 1)/2


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        results.append(solve(n))

    for result in results:
        print result
