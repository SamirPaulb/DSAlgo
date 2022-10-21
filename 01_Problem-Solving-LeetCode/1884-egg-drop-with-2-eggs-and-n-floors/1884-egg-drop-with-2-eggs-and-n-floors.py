class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp = [[-1]*5 for i in range(n+5)]
        
        def solve(e, n):
            if n == 0 or n == 1: return n
            if e == 1: return n
            
            if dp[n][e] != -1: return dp[n][e]
            
            ans = 2**31
            for f in range(1, n+1):
                tmp = 1 + max(solve(e-1, f-1), solve(e, n-f))
                ans = min(ans, tmp)
            dp[n][e] = ans
            return dp[n][e]
        
        return solve(2, n)