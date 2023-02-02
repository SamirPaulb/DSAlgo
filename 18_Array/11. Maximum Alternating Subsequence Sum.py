# https://leetcode.com/problems/maximum-alternating-subsequence-sum/

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        stack = []
        for n in nums:
            if not stack:
                stack.append(n)
                continue
            elif len(stack)%2 and stack[-1] <= n:  # Odd index
                stack.pop()
            elif not len(stack)%2 and stack[-1] >= n:  # even index
                stack.pop()
            stack.append(n)
                
        if not len(stack)%2:
            stack.pop()

        # print(stack)
        res = 0
        for i in range(1, len(stack)+1):
            if i%2:
                res += stack[i-1]
            else:
                res -= stack[i-1]
        
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
