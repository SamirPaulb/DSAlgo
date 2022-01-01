# https://www.youtube.com/watch?v=UmMh7xp07kY&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=9
# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        equalSum = s // 2
        if s % 2 != 0: return False
        n = len(nums)
        dp = [[False] * (equalSum + 1) for i in range(n + 1)]
        # Change the first row => arr is empty => No subset is there for any sum > 0
        for j in range(equalSum + 1):
            dp[0][j] = False
        # Change the first column => target sum is 0 => for any subset sum can be equal to 0
        for i in range(n + 1):
            dp[i][0] = True
        # Change the value of remaining dp matrix
        for i in range(1, n + 1):
            for j in range(1, equalSum + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
                            
        return dp[-1][-1]
        