class Solution:
    def integerReplacement(self, n: int) -> int:
        memo = {}
        
        def solve(n):
            if n == 1: return 0
            if n in memo: return memo[n]
            ans = 0
            if n % 2 == 0: ans = 1 + solve(n//2)
            else: ans = 1 + min(solve(n+1), solve(n-1))
            memo[n] = ans
            return ans
        
        return solve(n)