__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/617/A

Solution: Keep the possible steps in decreasing order so that when we use them, we always try to use the larger step 
first, thereby minimizing the steps needed. Now iterate till n is positive and use the possible steps to decrement n.
Return the count of steps in the end. 
'''

steps = (5, 4, 3, 2, 1)


def solve(n):

    stepsCount = 0
    while n > 0:

        for step in steps:

            if n >= step:
                stepsCount += 1
                n -= step
                break

    return stepsCount


if __name__ == "__main__":

    n = int(raw_input())
    print solve(n)

