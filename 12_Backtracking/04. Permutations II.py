# https://leetcode.com/problems/permutations-ii/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        def dfs(arr, path):
            if not arr:
                res.append(path)
            for i in range(len(arr)):
                if i > 0 and arr[i] == arr[i-1]:
                    continue
                dfs(arr[:i] + arr[i+1:], path + [arr[i]])
            
        dfs(nums, [])
        return res

# Time: O(N^2)    # as for each element we are making (n-1) traversal again
# Space: O(N)     # as we are creating n-1 subarrays