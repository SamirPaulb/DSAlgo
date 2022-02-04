# https://leetcode.com/problems/unique-binary-search-trees/
# https://youtu.be/H1qjjkm3P3c
class Solution:
    def numTrees(self, n: int) -> int:
        '''
        # Recursive Solution 
        def solve(n):
            if n <= 1: return 1
            if n == 2: return 2
            if n == 3: return 5
            ans = 0
            for i in range(n):
                ans += solve(i) * solve(n-i-1)
            return ans
        
        return solve(n)
        '''
        # Dynamic Programming
        dp = [0] * (n+1)
        dp[0] = 1
        
        for i in range(1, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]
                
        return dp[-1]

# Time: O(n*n)
# Space: O(n)