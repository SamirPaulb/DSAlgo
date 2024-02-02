# https://www.lintcode.com/problem/1307/
# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/description/

from typing import List

# Approach 1: Backtracking
# Time: O(n)
# Space: O(h)
class Solution:
    def verify_preorder(self, preorder):
        i = 0

        def dfs(min, max):
            nonlocal i
            if i == len(preorder): return
            if preorder[i] < min or preorder[i] > max: return 

            val = preorder[i]
            i += 1
            dfs(min, val)
            dfs(val, max)
        
        dfs(float('-inf'), float('inf'))
        return i == len(preorder)


# Approach 2: Stack
# Time: O(n)
# Space: O(n)
class Solution:
    def verify_preorder(self, preorder):
        low = float('-inf')
        stack = []
        
        for p in preorder:
            if p < low: return False
            while stack and stack[-1] < p:
                low = stack.pop()
            stack.append(p)
        
        return True
