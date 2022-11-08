__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/732/B

Solution: Greedy approach. Iterate over the array and take the sum of current and
previous element. If that is smaller than k, then we add the diff to current cell.
Adding to current cell is a greedy choice since that helps in handling the next
pair of cells too. The total of those diffs added and the updated array are the
final answers.
'''


def solve(n, k, arr):

    all_needed = 0
    for i in xrange(1, n):

        curr_needed = k - (arr[i-1] + arr[i])
        if curr_needed > 0:
            arr[i] += curr_needed
            all_needed += curr_needed

    print all_needed
    print " ".join(str(_) for _ in arr)


if __name__ == "__main__":

    n, k = map(int, raw_input().split(" "))
    arr = map(int, raw_input().split(" "))
    solve(n, k, arr)
