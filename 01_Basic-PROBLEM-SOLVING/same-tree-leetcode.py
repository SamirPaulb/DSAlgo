# https://leetcode.com/problems/same-tree/
# 100. Same Tree
'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

Input: p = [1,2,1], q = [1,1,2]
Output: false

'''



class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        elif (not p and q) or (p and not q) or (p.val != q.val): return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
