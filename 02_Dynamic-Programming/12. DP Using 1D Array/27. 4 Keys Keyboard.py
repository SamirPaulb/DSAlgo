# https://www.lintcode.com/problem/867

class Solution:
    def max_a(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        for i in range(4, n+1):
            count = 2
            prev = i-3
            while prev > 0:
                dp[i] = max(dp[i], count*dp[prev])
                prev -= 1
                count += 1
        return dp[n]


# Time: O(N^2)
# Space: O(N)
