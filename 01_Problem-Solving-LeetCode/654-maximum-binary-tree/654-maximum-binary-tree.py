# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None
        
        maxV = max(nums)
        maxI = nums.index(maxV)
        
        root = TreeNode(maxV)
        root.left = self.constructMaximumBinaryTree(nums[:maxI])
        root.right = self.constructMaximumBinaryTree(nums[maxI+1:])
        
        return root