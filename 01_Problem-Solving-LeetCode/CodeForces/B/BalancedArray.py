__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1343/B

Solution: The question has a few conditions and we shall need to exploit odd-even numbers' properties to handle that.

We know that 2 odd numbers can sum to make an even number. Hence for n sized array, if we put n/2 even and n/2 odd 
numbers, those n/2 odd numbers should for pairs to sum to even so that jointly that can be equal to the sum of even side
which would be even anyways. Therefore, the even half (or odd half) should at least be even as well. In other words, 
the smallest array possible can be of size 4, and all possible array sizes have to be multiples of 4. This can take care
of the "NO" condition.

Now for the actual numbers, we can use the natural numbers from 1 to n-1 to build the even half and one less than odd
half of the numbers. Every even number differs by 1 from its odd neighbors. Hence if we have n = 8

2, 4, 6, 8, 1, 3, 5, x can be the possible solution. Now the question arises what should x be. 
For that lets decompose the numbers.

2, 4, 6, 8, 1, 3, 5, x 

2, 4, 6, 8, 2-1, 4-1, 6-1, x

So if we generalize, 

2, 4,....n, 2-1, 4-1, .... x

So 
The even numbers sum is (2 + 4 + .... n)  
The odd numbers sum is (2-1 + 4-1 + .... x) 
=  (2 + 4 + .... x) - 1* (n/2 - 1)

Since the even and odd numbers sum is required to be same, we can equate the LHS and RHS here:

(2 + 4 + .... n)  = (2 + 4 + .... x) - 1* (n/2 - 1)
n + 1* (n/2 - 1) = x

(3n - 2)/2 = x

So for n = 8, x = 11

Note that this is just a strategy that we can use to find the desired array. I suppose there can be other ways as well. 
  
'''


def solve(n):

    if n % 4 != 0:
        return "NO"

    evenHalf = ""
    for i in xrange(1, n/2 + 1):
        evenHalf += str(2 * i) + " "

    oddHalf = ""
    for i in xrange(1, n/2):
        oddHalf += str((2 * i) - 1) + " "
    oddHalf += str((3*n - 2)/2)

    return "YES" + "\n" + evenHalf + oddHalf


if __name__ == "__main__":
    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        results.append(solve(n))

    for result in results:
        print result
