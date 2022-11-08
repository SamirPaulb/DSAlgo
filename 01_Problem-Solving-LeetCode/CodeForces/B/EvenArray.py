__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1367/B

Solution: The idea is to find two counts: First, the odd numbers present at even indices and second, even numbers 
present at odd indices. For the array to turn good, the swaps have to happen between these wrongly placed numbers, i.e
for an odd number placed at even index, there should be its counterpart (even number placed at odd index). Hence these
two counters should be equal. Return -1 if they are not, and otherwise, it is equal to the count of those wrongly
placed numbers. 
'''


def solve(n, arr):

    odd_nos_at_even_idx = even_nos_at_odd_idx = 0

    for i in xrange(0, n):

        if i % 2 == 0 and arr[i] % 2 != 0:
            odd_nos_at_even_idx += 1
        elif i % 2 != 0 and arr[i] % 2 == 0:
            even_nos_at_odd_idx += 1

    return -1 if odd_nos_at_even_idx != even_nos_at_odd_idx else odd_nos_at_even_idx


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):

        n = int(raw_input())
        arr = map(int, raw_input().split(" "))
        results.append(solve(n, arr))

    for result in results:
        print result
