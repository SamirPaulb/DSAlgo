# https://www.lintcode.com/problem/650
# https://leetcode.com/problems/find-leaves-of-binary-tree/description/

# Find the height using postorder traversal -> leaves height is 0 

class Solution:
    def findLeaves(self, root):
        heightDict = {}

        def tree_height(root):
            if not root: return 0
            lh = tree_height(root.left) 
            rh = tree_height(root.right)
            h = 1 + max(lh, rh)
            if h not in heightDict: heightDict[h] = []
            heightDict[h].append(root.val)
            return h
        
        tree_height(root)
        return list(heightDict.values())

# Time: O(N)
