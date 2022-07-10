# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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

    
''' 
# Time: O(N*N!)
# Space: O(N!)

Explanation: https://leetcode.com/problems/permutations/discuss/993970/Python-4-Approaches-%3A-Visuals-%2B-Time-Complexity-Analysis
'''
