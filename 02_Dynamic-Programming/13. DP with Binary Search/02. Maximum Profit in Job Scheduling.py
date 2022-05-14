# https://leetcode.com/problems/maximum-profit-in-job-scheduling/

import bisect

class Solution:
    def jobScheduling(self, S, E, profit):
        jobs = sorted(list(zip(S, E, profit)))
        S = [i[0] for i in jobs]
        n = len(jobs)
        dp = [0] * (n + 1)

        for k in range(n-1,-1,-1):
            temp = bisect_left(S, jobs[k][1])
            dp[k] = max(jobs[k][2] + dp[temp], dp[k+1])

        return dp[0]


# Time complexity is O(n * log n), because we do n binary searches. Space complexity is O(n)