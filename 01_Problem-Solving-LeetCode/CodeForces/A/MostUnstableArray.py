__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1353/A

Solution: The question basically requires finding a pattern of how the desierd array can be constructed. 

Let's go over case by case to formulate the pattern.

CASE A: n = 1, m = 100
Since there is exactly one element, we can never get the absolute difference of neihbors (since there are none). So the
answer for n = 1 would always be 0. 

CASE B: n = 2, m = 100
Since we can only use non-negative numbers (basically whole numbers), we have just one way to construct the array. That
is [0, 100] or [100, 0]. This way we can do the difference of 1 pair of neighbors and get the result which will always be 
m. 

Case C: n = 5, m = 6
Using the knowledge of sandwiching 0s at adjacent positions in the array, lets try to construct this array.

[0, 6, 0, 0, 0] 
With this config, we can get only 2 neighbor pairs with non-zero diff-sum which is |0 - 6| + |6 - 0| = 12

Let's take 1 from the 6 and put it at the adjacent position.
[0, 5, 0, 1, 0]
Now we have |0 - 5| + |5 - 0| + |0 - 1| + |1 - 0| = 12

Let's take 2 from the 6 and put it at the adjacent position.
[0, 4, 0, 2, 0]
Now we have |0 - 4| + |4 - 0| + |0 - 2| + |2 - 0| = 12

Let's take 3 from the 6 and put it at the adjacent position.
[0, 3, 0, 3, 0]
Now we have |0 - 3| + |3 - 0| + |0 - 3| + |3 - 0| = 12

So any of these configs are correct but effectively we constructed them from its root config of 
[0, 6, 0, 0, 0] or in generalization [0, m, 0, 0, 0]

Now we see that max diff-sum would be 2*m since that element m can have its difference with its left and right neighbor. 

So we can generalize that it would always ne 2m for n > 2.  

'''


def solve(n, m):

    if n == 1:
        return 0
    elif n == 2:
        return m
    else:
        return 2*m


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n, m = map(int, raw_input().split(" "))
        results.append(solve(n, m))

    for result in results:
        print result
