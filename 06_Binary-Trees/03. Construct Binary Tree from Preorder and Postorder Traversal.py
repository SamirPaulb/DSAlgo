# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
# https://youtu.be/LnHSOy7ctms

# Method - 1 => Most Efficient
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        preInd = {v:i for i, v in enumerate(preorder)}
        def solve(l, r, postorder):
            if l == r: return None
            if r-l == 1: return TreeNode(postorder.pop())
            root = TreeNode(postorder.pop())
            i = preInd[postorder[-1]]
            root.right = solve(i, r, postorder)
            root.left = solve(l+1, i, postorder)
            return root
        
        return solve(0, len(preorder), postorder)
    


class Solution:
    def constructFromPrePost(self, preorder, postorder):
        self.preIndex = 0
        def dfs(postStart, postEnd):
            if postStart > postEnd or self.preIndex >= len(preorder): return None
            root = TreeNode(preorder[self.preIndex])
            self.preIndex += 1
            if postStart == postEnd or self.preIndex >= len(preorder): return root
            postIndex = postorder.index(preorder[self.preIndex])
            root.left = dfs(postStart, postIndex)
            root.right = dfs(postIndex+1, postEnd-1)
            
            return root
        
        return dfs(0, len(preorder))



# Method - 3
class Solution:
    def constructFromPrePost(self, preorder, postorder):
        
        def dfs(preorder, postorder):
            if postorder:
                if len(postorder) == 1:
                    return TreeNode(preorder.pop(0))
                root = TreeNode(preorder.pop(0))
                i = postorder.index(preorder[0])
                root.left = dfs(preorder, postorder[:i+1])
                root.right = dfs(preorder, postorder[i+1:-1])
                return root
        
        return dfs(preorder, postorder)
    
