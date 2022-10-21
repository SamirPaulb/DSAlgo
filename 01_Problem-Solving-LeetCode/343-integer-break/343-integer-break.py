class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0, 1]
        
        for m in range(2, n+1):
            r = m-1
            l = 1
            val = 0
            while r >= l:
                val = max(val, max(r, dp[r])*max(l, dp[l]))
                r -= 1
                l += 1
            dp.append(val)
        
        return dp[-1]