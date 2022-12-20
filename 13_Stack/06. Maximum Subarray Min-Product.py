# https://leetcode.com/problems/maximum-subarray-min-product/

# 84. Largest Rectangle in Histogram

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        leftBound = [0] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack: leftBound[i] = stack[-1] + 1
            stack.append(i)
        
        rightBound = [n-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack: rightBound[i] = stack[-1] - 1
            stack.append(i)
        
        prefixSum = []
        s = 0
        for i in range(n):
            s += nums[i]
            prefixSum.append(s)
        
        res = 0
        for i in range(n):
            lb = leftBound[i]
            rb = rightBound[i]
            s = prefixSum[rb] - prefixSum[lb] + nums[lb]
            res = max(res, nums[i] * s)
        # print(leftBound)
        # print(rightBound)
        # print(prefixSum)
        return res % (10**9 + 7)
            
