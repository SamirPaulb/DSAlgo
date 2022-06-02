# https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1/
# https://youtu.be/0ca1nvR0be4

class Solution:
    def printBoundaryView(self, root):
        
        def addLeftBoundary(root, res):
            ans = []
            cur = root
            while cur:
                ans.append(cur.data)
                if cur.left: cur = cur.left
                else: cur = cur.right
            res += ans[:-1]

        def addLeafNodes(root, res):
            if not root: return
            if not root.left and not root.right: res.append(root.data)
            addLeafNodes(root.left, res)
            addLeafNodes(root.right, res)

        def addRightBoundary(root, res):
            ans = []
            cur = root
            while cur:
                ans.append(cur.data)
                if cur.right: cur = cur.right
                else: cur = cur.left
            res += ans[:-1][::-1]
            
        res = []
        if not root: return res
        res.append(root.data)
        if not root.left and not root.right: return res
        addLeftBoundary(root.left, res)
        addLeafNodes(root, res)
        addRightBoundary(root.right, res)
        return res
        
        
# Time: O(N)
# Space: O(N)
        
