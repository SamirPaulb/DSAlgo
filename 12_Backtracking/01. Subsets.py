# https://leetcode.com/problems/subsets/

# -------------------------------------------- Method 1 ---------------------------------------------------------
# DFS => Without taking subset as Global variable        
class Solution:
    def subsets(self, nums):        
        res = []
        def dfs(i, subset):
            if i >= len(nums):
                res.append(subset)
                return    # to stop this call here so this will not call another 2 dfs
            dfs(i+1, subset + [nums[i]])  # calling dfs Including nums[i] in subset
            # as every subset is using different subset array so we don't need to pop
            dfs(i+1, subset)     # calling dfs Excluding nums[i] in subset
        
        dfs(0, [])
        return res
'''
Time Complexity: O(N * 2^N)  ; because there will be 2^N different subsets, and we have to create a copy of each one, which is O(N).
Space Complexity: O(N)  ; if you don't count the output array, because the size of the function call stack will be O(N). Meaning we have to call the recursive function N times in a row, before it returns.
'''

# -------------------------------------------- Method 2 ---------------------------------------------------------
# DFS => Taking subset as a Global variable
# https://youtu.be/REOH22Xwdkk
class Solution:
    def subsets(self, nums):
        res = []
        subset = []  # Global variable to use in all dfs calls
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())  # appending a copy of original global subset 
                return  # to stop this call here so this will not call another 2 dfs
            subset.append(nums[i]) # include nums[i]
            dfs(i+1)  # calling dfs Including nums[i] in subset
            subset.pop() # removing nums[i] as we will use subset to call dfs without including nums[i]
            dfs(i+1) # calling dfs Excluding nums[i] in subset
        
        dfs(0)
        return res
'''
Time Complexity: O(N * 2^N)  ; because there will be 2^N different subsets, and we have to create a copy of each one, which is O(N).
Space Complexity: O(N)  ; if you don't count the output array, because the size of the function call stack will be O(N). Meaning we have to call the recursive function N times in a row, before it returns.
''' 

# -------------------------------------------- Method 3 ---------------------------------------------------------
# BFS
class Solution:
    def subsets(self, nums):
        res = [[]]
        for n in nums:
            res += [r + [n] for r in res]
        return res

# Time: O(N * 2^N)
# Space: O(N)