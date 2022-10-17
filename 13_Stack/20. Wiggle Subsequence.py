# https://leetcode.com/problems/wiggle-subsequence/


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        flag = 1
        stack = [nums[0]]
        i = 1
        while i < len(nums) and nums[i] == nums[i-1]:
            i += 1
        if i < len(nums):
            if nums[i-1] > nums[i]: flag = -1
            stack.append(nums[i])
            
        for num in nums[i+1:]:
            if num == stack[-1]: continue
            if flag == 1:   # Increasing
                if num > stack[-1]: stack.pop()
                else: flag *= -1
            else:           # flag = -1 => Decreasing
                if num < stack[-1]: stack.pop()
                else: flag *= -1
            stack.append(num)
        
        return len(stack)
      
      
# Time: O(n)
# Space: O(n)
