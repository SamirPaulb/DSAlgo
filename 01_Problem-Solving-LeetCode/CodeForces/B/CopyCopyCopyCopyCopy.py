__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1325/B

Solution: Since we can make n copies of the array, we can pick the smallest element in first
copy, second smallest in second copy and so on. This way we can construct the longest strictly
increasing sub-sequence from the copy array. Therefore, the number of distinct elements in the
original array would bound the length of this sub-sequence. We find that via a set and return its
length as the final answer.  
'''


def solve(n, arr):

    distinct = set()

    for i in xrange(0, n):
        distinct.add(arr[i])

    return len(distinct)


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        arr = map(int, raw_input().split(" "))
        results.append(solve(n, arr))

    for result in results:
        print result
