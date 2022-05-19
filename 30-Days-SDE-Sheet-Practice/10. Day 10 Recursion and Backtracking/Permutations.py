# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def solve(nums, path):
            if not nums: 
                res.append(path)
                return
            
            for i in range(len(nums)):
                solve(nums[:i] + nums[i+1:], path + [nums[i]])
            
        solve(nums, [])
        return res

# Time: (n * n!) # as we are generating each pernutation and traversing the array
# Space: O(n!)   # n factorial as we are generating each permutation