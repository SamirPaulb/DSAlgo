# https://leetcode.com/problems/ugly-number-ii/
# https://youtu.be/X5SuOsIWCoI

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        p2 = p3 = p5 = 0
        
        for i in range(1, n):
            twoMultiple = dp[p2] * 2
            threeMultiple = dp[p3] * 3
            fiveMultiple = dp[p5] * 5
            dp[i] = min(twoMultiple, threeMultiple, fiveMultiple)
            
            if dp[i] % twoMultiple == 0: p2 += 1
            if dp[i] % threeMultiple == 0: p3 += 1
            if dp[i] % fiveMultiple == 0: p5 += 1
        
        return dp[-1]
