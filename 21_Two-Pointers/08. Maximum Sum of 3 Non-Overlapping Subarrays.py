# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/
# https://youtu.be/mXeT7-oZeQQ

'''
First Solve: Maximum Sum of Two Non-Overlapping Subarrays

move a window of size k between left and right parts and check maxsum
'''

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        prefixSum = []
        s = 0
        for i in nums:
            s += i
            prefixSum.append(s)

        n = len(nums)
        left = [(0,0)] * n
        for i in range(k-1, n-2*k):
            curSum = prefixSum[i] - prefixSum[i-k+1] + nums[i-k+1]
            if i>0: left[i] = left[i-1]
            if curSum > left[i][0]:
                left[i] = (curSum, i-k+1)
        
        right = [(0,0)] * n
        for i in range(n-k, 2*k-1, -1):
            curSum = prefixSum[i+k-1] - prefixSum[i] + nums[i]
            if i+1 < n: right[i] = right[i+1]
            if curSum >= right[i][0]:
                right[i] = (curSum, i)
        
        res = []
        maxSum = 0
        for i in range(k, n-k):
            l = i-1
            r = i+k
            curSum = left[l][0] + (prefixSum[r-1] - prefixSum[l]) + right[r][0]
            if curSum > maxSum:
                maxSum = curSum
                res = [left[l][1], i, right[r][1]]
        # print(prefixSum)
        # print(left)
        # print(right)
        return res
        
                
            
# Time: O(N)
# Space: O(N)
