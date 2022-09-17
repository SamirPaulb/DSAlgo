# https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

'''
# Intuition
Assume the array has only 0 and 1.
Then the question changes:
If A[i] = 1, shortest array is [A[i]], length is 1.
If A[i] = 0, we need to find the index j of next 1,
then j - i + 1 is the length of shortest subarray.
If no next 1, 1 is the length

To solve this problem,
we can iterate the array reversely
and keep the index j of last time we saw 1.
res[i] = max(1, last - i + 1)
'''

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lastIndex = [0] * 32
        res = [1] * n
        
        for i in range(n-1, -1, -1):
            for j in range(32):
                if nums[i] & (1 << j):
                    lastIndex[j] = i
            # print(lastIndex)
            res[i] = max(1, max(lastIndex) - i + 1)
        
        return res
    
    
    
    
# Time: O(N)
# Space: O(N)
