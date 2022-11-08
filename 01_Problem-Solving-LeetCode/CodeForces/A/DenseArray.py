__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1490/A

Solution: Say we are assessing the pair arr[i] and arr[i+1] of the given array and their max and min are pair_max and
pair_min respectively.  
The condition to satisfy between this pair of elements in the array for it to be dense is:

pair_max / pair_min <= 2 
=> pair_max  <= 2 * pair_min

Therefore, the as long as the above condition is held, we don't need to add elements. If 2 * pair_min > pair_max, we
need to add a new element which should be 2 * pair_min. We continue to do this till the condition of dense array is not
satisfied. The number of iterations done to get this condition satisfied is the total number of elements needed in between
the original pair of elements (arr[i], arr[i+1]). Return this count as the final answer.   

'''
import math


def solve(n, arr):

    elems_needed = 0

    for i in xrange(0, n-1):

        pair_max = max(arr[i], arr[i+1])
        pair_min = min(arr[i], arr[i+1])

        while 2 * pair_min < pair_max:

            pair_min *= 2
            elems_needed += 1

    return elems_needed


if __name__ == "__main__":

    t = int(raw_input())

    for _ in xrange(0, t):
        n = int(raw_input())
        arr = map(int, raw_input().split(" "))
        print solve(n, arr)
