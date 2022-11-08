__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1348/A

Solution: If the constraint of n/2 coins on both piles wasn't there, we would put the heaviest coin (2^n) in one pile
while the others on the second pile. But since we have that constraint, we extend this idea by including the heaviest
coin on the first pile, we add n/2 - 1 lightest coins on it. The remaining heavier coins are on the other pile. The
difference of these weights in the final result. 

We avoid using the inbuilt pow() by using bitwise operators (left shift 1 is equivalent to 2 powers) 
Also, avoid abs() method by always subtract pile2 from pile1. Since we have the heaviest coin on the pile1, it will 
always be the heavier from pile2.  
'''


def solve(n):

    pile1 = pile2 = 0

    pile1 += (1 << n)
    for i in xrange(1, n/2):
        pile1 += (1 << i)

    for i in xrange(n/2, n):
        pile2 += (1 << i)

    return pile1 - pile2


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):

        n = int(raw_input())
        results.append(solve(n))

    for result in results:
        print result
