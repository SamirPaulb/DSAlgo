# https://leetcode.com/problems/132-pattern/
# https://youtu.be/q5ANAl8Z458

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        curMin = nums[0]
        stack = []  # stack contains [nums[i], nums[j]] and n = nums[k] 
        
        for n in nums[1:]:
            while stack and n >= stack[-1][1]:
                stack.pop()
            if stack and n > stack[-1][0]: return True
            stack.append([curMin, n])
            curMin = min(curMin, n)
        
        return False
      
      
      
