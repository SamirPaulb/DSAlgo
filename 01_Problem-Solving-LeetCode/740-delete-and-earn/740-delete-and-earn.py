class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums: return 0
        
        arr = [0]*(max(nums)+1)
        
        for i in nums:
            arr[i] += i
        
        dp = [0]*(len(arr))
        
        for i in range(len(arr)):
            if i == 0:
                dp[i] =  0
            elif i == 1:
                dp[i] = max(arr[i], dp[i-1])
            else:
                dp[i] = max(arr[i] + dp[i-2], dp[i-1])
        
        return dp[-1]