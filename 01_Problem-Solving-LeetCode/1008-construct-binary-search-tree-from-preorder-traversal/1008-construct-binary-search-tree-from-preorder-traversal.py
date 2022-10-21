# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        parent = root
        
        for nodeVal in preorder[1:]:
            newNode = TreeNode(nodeVal)
            if stack and newNode.val < stack[-1].val:
                parent.left = newNode
                stack.append(newNode)
                parent = stack[-1]
            else:
                while stack and stack[-1].val < newNode.val:
                    parent = stack.pop()
                parent.right = newNode
                stack.append(newNode)
                parent = stack[-1]
        
        return root