class Solution:
    
    def findGCD(self, nums: List[int]) -> int:
        a = max(nums)
        b = min(nums)
        
        dp = [[-1]*(a + 1) for i in range(a + 1)]
        def gcd(a, b):
            if a == 0 : return b
            if b == 0: return a
            if a == b: return a
            if dp[a][b] != -1: return dp[a][b]
            if a < b: 
                dp[a][b] = gcd(a, b-a)
            else:
                dp[a][b] = gcd(b, a-b)
            
            return dp[a][b]
        
        
        return gcd(a, b)