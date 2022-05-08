# https://leetcode.com/problems/next-permutation/
''' 
Next Permutation = elemtnt Just Greater than the current element.
So find the elemnt from traversing from end. if nums[i] > nums[i-1] we can swap these and get the 
value. but there may any greater element in right. 
'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # find out swap point
        sp = -1; n = len(nums)
        for i in range(1, n):
            if nums[i] > nums[i - 1]: sp = i
        
        if sp == -1: # Swap point exist ie. nums = [5, 4, 3, 2, 1]
            return nums.reverse()
        
        # checking wheather any i, i > sp for which nums[i] > nums[sp - 1]
        # ie. nums = [1, 2, 3, 5, 4, 2]
        lsp, rsp = sp - 1, sp # Left Swap point, Right swap point
        for i in range(sp+1, n):
            if nums[i] > nums[lsp]: rsp = i
        
        nums[lsp], nums[rsp] = nums[rsp], nums[lsp]
        
        l, r = sp, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1; r -= 1
        
        return nums

# Time: O(N)
# Space: O(1)