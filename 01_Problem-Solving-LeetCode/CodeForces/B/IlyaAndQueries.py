__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/313/B

Solution: We keep an increasing dp array which tracks the count of s_i = s_i+1 condition met
so far. So its an increasing array. For a given range of [L,R), we calculate the answer as
dp[R] - dp[L]. Since the query ranges are given 1-indexed, we need to subtract one from them
to query from the dp array.  
'''


def solve(s, ranges):

    n = len(s)
    dp = [0] * n

    curr_len = 0
    for i in xrange(1, n):
        if s[i] == s[i-1]:
            curr_len += 1
        dp[i] = curr_len

    results = list()
    for range in ranges:
        results.append(dp[range[1]-1] - dp[range[0]-1])

    return "\n".join(str(_) for _ in results)


if __name__ == "__main__":

    s = raw_input()
    m = int(raw_input())

    ranges = list()
    for _ in xrange(0, m):

        range = map(int, raw_input().split(" "))
        ranges.append(range)

    print solve(s, ranges)
