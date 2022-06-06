# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        parent = root
        stack = [parent]
        
        for v in preorder[1:]:
            newNode = TreeNode(v)
            if stack and newNode.val < parent.val:
                parent.left = newNode
                stack.append(newNode)
                parent = newNode
            else:
                while stack and stack[-1].val < newNode.val:
                    parent = stack.pop()
                parent.right = newNode
                stack.append(newNode)
                parent = newNode
        
        return root
    
    
# Time: O(N)
# Space: O(N)
