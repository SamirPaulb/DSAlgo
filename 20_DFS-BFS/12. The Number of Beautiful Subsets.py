# https://leetcode.com/problems/the-number-of-beautiful-subsets/

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.res = 0
        nums.sort()
        seen = set()
        
        def dfs(subset, i):
            if i >= len(nums):
                if len(subset) > 0: self.res += 1
                return 
            if nums[i] - k not in seen:
                seen.add(nums[i])
                dfs(subset + [nums[i]], i+1)
                seen.discard(nums[i])
            dfs(subset, i+1)
        
        dfs([], 0)
        return self.res
    
    
# Time: O(2^n)    

''' NOTE:
The discard() method removes the specified item from the set. This method is different from the remove() method, 
because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.
'''
