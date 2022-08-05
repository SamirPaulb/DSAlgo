# https://leetcode.com/problems/maximum-width-ramp/

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # nums = [9,8,1,0,1,9,4,0,4,1]
        # arr = [0, 1, 2, 3]
        arr = []  # array in indeices Sorted in decreasing order of elements
        for i, ch in enumerate(nums):
            if not arr or nums[arr[-1]] > nums[i]:
                arr.append(i)
        
        res = 0
        i = len(nums)-1
        while arr and i > 0:
            if arr and nums[arr[-1]] <= nums[i]:
                res = max(res, i - arr.pop())
            else:
                i -= 1
        
        return res  # 7
    
    
# Time: O(n)
# Space: O(n)




class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        '''
        # Brute Force   # Time: O(N^2)
        res = 0
        for i in range(len(nums)):
            for j in range(i+1):
                if nums[i] >= nums[j]:
                    res = max(res, i-j)
                    break
                    
        return res
        '''
        
        '''
        # Method 1   # Time: O(N log(N))
        # Keep a decreasing stack.For each number, binary search the first smaller number in the stack. When the number is smaller the the last, push it into the stack.
        stack = []
        res = 0
        for i in range(len(nums)-1, -1, -1):
            if not stack or nums[stack[-1][1]] < nums[i]:
                stack.append([nums[i], i])
            else:
                j = stack[bisect.bisect(stack, [nums[i], i])][1]
                res = max(res, j - i)
        
        return res
        '''
        
        # Method 2   # Time: O(N)
        # make a stack in decreasing order
        stack = []
        res = 0
        for i in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        
        # Now traverse from end and check. 
        # as we want max length so firstly popped element will give max length
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                res = max(res, i - stack.pop())
        
        return res
