__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1360/B

Solution: Sort the numbers in strength list so that the neighbors are the numerically closest numbers. Now we need
to find the smallest difference of neighbors. One of that pair would be list A's max and other would be list B's min. 
'''


def solve(n, strength):

    strength.sort()

    min_diff = strength[1] - strength[0]
    for i in xrange(2, n):

        min_diff = min(min_diff, strength[i] - strength[i-1])

    return min_diff


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        strength = map(int, raw_input().split(" "))
        results.append(solve(n, strength))

    for result in results:
        print result
