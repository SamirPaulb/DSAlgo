# https://leetcode.com/problems/maximum-alternating-subsequence-sum/

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            if not stack:
                stack.append(num)
                continue
            elif len(stack)%2 == 1 and stack[-1] <= num:    
                stack.pop() # current num is greater than even index num
            elif len(stack)%2 == 0 and stack[-1] >= num:    
                stack.pop() # current num is smaller than odd index num 
            stack.append(num)
            
        if len(stack)%2 == 0: stack.pop()   # remove odd index value
            
        res = 0
        for i in range(len(stack)):
            if i%2 == 0:
                res += stack[i]
            else:
                res -= stack[i]
        
        return res
    
# Time: O(N)
# Space: O(N)



'''
Given an alternating sequence (a0, a1... ak), the change in value after appending an element x depends only on whether we have an even or odd number of elements so far:

If we have even # of elements, we add x; otherwise, we subtract x. So, tracking the best subsequences of odd and even sizes gives an extremely simple update formula.

'''
class Solution:
    def maxAlternatingSum(self, nums):
        odd, even = nums[0], 0
        for num in nums[1:]:
            odd = max(even + num, odd)
            even = max(odd - num, even)
        
        return max(odd, even)
 
# Time: O(N)
# Space: O(1)
