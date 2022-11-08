__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1005/A

Solution: Iterate over the array of steps and check if the current step differs by exactly 1 from the
previous step. If not, we completed a complete step in the previous index and capture its value in a list.
Finally the values in the list along with the length of this list is the answer. 
'''


def solve(n, arr):

    step_vals = list()

    for i in xrange(1, n):
        if arr[i] - arr[i-1] != 1:
            step_vals.append(arr[i-1])
    step_vals.append(arr[n-1])

    print len(step_vals)
    print " ".join(str(_) for _ in step_vals)


if __name__ == "__main__":

    n = int(raw_input())
    arr = map(int, raw_input().split(" "))
    solve(n, arr)
