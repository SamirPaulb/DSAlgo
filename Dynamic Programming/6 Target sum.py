# https://www.youtube.com/watch?v=Hw6Ygp3JBYw&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=12
# https://leetcode.com/problems/target-sum/
'''
Assigning + and - before elements of nums such that sum of all elements is equal to target
Basically we are again deviding the array into 2 subsets such that diffrence between that subsets equal to target
s1 - s2 = target    ---(1)
s1 + s2 = sum(nums) ---(2)
(1) + (2)
s1 = (target + sum(nums)) // 2
Now we have to find number of possible subsets s1 in nums
'''

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if abs(target) > sum(nums): return 0  # nums = [10], target = -100
        s1 = (target + sum(nums)) // 2
        # 2 * s1 = (target + sum(nums))  => as (target + sum(nums)) is a multiple of 2 so it must be an even number
        if (target + sum(nums)) % 2 != 0: return 0
        dp = [[0]*(s1+1) for i in range(len(nums) + 1)]
        # 1st row of dp = 0; as in 1st row size of nums = [] so no subset s1 is possile for sum(s1) > 0
        for j in range(s1 + 1):
            dp[0][j] = 0
        # 1st column of dp = 1; as in 1st column sum(s1) = 0; so empty nums is possibel so 1 possible subset s1 everytime
        for i in range(len(nums)+1):
            dp[i][0] = 1
        # change values of remaining dp starting from (1, 0) to (len(nums), s1)
        for i in range(1, len(nums) + 1):
            for j in range(s1 + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[-1][-1] # dp[len(nums)][s1]
    