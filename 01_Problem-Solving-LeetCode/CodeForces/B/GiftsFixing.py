__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1399/B

Solution: Since we cannot add objects, the only way to make them equal is to eat (in other words, reduce). Hence the 
target candy and orange count should be the minimum in their respective lists. Once those have been determined, we 
iterate over each pair (i.e. a gift), and calculate the difference of the current value and the target of its kind. The
max of them would be the moves need to equalize this gift. The sum of all such moves is the final answer.  
'''


def solve(n, arr_a, arr_b):

    target_a = arr_a[0]
    target_b = arr_b[0]
    for i in xrange(1, n):
        target_a = min(target_a, arr_a[i])
        target_b = min(target_b, arr_b[i])

    moves = 0
    for i in xrange(0, n):

        diff_a = arr_a[i] - target_a
        diff_b = arr_b[i] - target_b

        moves += max(diff_a, diff_b)

    return moves


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        arr_a = map(int, raw_input().split(" "))
        arr_b = map(int, raw_input().split(" "))
        results.append(solve(n, arr_a, arr_b))

    for result in results:
        print result
