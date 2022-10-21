class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0: return False
        target = sum(nums) // 2
        
        dp = [[False]*(target+1) for i in range(len(nums)+1)]
        
        for i in range(len(nums)+1):
            dp[i][0] = True
        
        for i in range(1, len(nums)+1):
            for j in range(1, target+1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]