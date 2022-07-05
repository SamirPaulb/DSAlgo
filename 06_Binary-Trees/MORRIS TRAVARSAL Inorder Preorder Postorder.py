# Morris Traversal Inorder
# https://leetcode.com/problems/binary-tree-inorder-traversal/
class Solution:
    def inorderTraversal(self, root):
        res = []
        cur = root
        
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                
                if pre.right == None:
                    pre.right = cur
                    cur = cur.left
                else:
                    res.append(cur.val)
                    cur = cur.right
                
        return res
    
# Time: O(N)
# Space: O(1)




# Morris Traversal Preorder
# https://leetcode.com/problems/binary-tree-preorder-traversal/
class Solution:
    def preorderTraversal(self, root):
        res = []
        cur = root
        
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                
                if pre.right == None:
                    pre.right = cur
                    res.append(cur.val)
                    cur = cur.left
                else:
                    cur = cur.right
                
        return res
    
# Time: O(N)
# Space: O(1)




# Morris traversal for Postorder
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        cur = root
        while cur:
            if not cur.right: 
                res.append(cur.val)
                cur = cur.left
            else:
                pre = cur.right
                while pre and pre.left and pre.left != cur:
                    pre = pre.left
                if not pre.left:
                    pre.left = cur
                    res.append(cur.val)
                    cur = cur.right
                else:
                    pre.left = None
                    cur = cur.left
                    
        res.reverse()
        return res
