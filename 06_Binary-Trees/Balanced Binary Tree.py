# https://leetcode.com/problems/balanced-binary-tree/

'''
class Solution:
    def isBalanced(self, root):
        if not root: return True
        return abs(self.height(root.left) - self.height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root):
        if not root: return 0
        return 1 + max(self.height(root.left), self.height(root.right))

# Time: O(N^2)
# Space: O(1)
'''

# https://youtu.be/QfJsau0ItOY

class Solution:
    def isBalanced(self, root):
        
        def dfs(root):
            if not root: return True, 0  
            
            lb, lh = dfs(root.left)      
            rb, rh = dfs(root.right)
            
            b = abs(lh - rh) <= 1 and lb and rb

            return b, 1 + max(lh, rh)
        
        b, h = dfs(root)
        return b
    
# Time: O(N)
# Space: O(1)