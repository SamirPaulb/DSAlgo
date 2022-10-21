class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if abs(target) > abs(s): return 0
        if (s + target) % 2 != 0: return 0
        s1 = (s + target) // 2
        
        dp = [[0]*(s1 + 1) for i in range(len(nums)+1)]
        
        for i in range(len(nums)+1):
            dp[i][0] = 1 
        
        for i in range(1, len(nums)+1):
            for j in range(s1+1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]