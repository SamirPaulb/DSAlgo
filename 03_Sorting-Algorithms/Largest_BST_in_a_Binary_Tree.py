# Return the size of the largest sub-tree which is also a BST
# Method - 1
'''
class Solution:
    def largestBst(self, root):
        def isBST(root, min, max):
            if not root: return True
            if min >= root.data: return False
            if max <= root.data: return False
            return isBST(root.left, min, root.data) and isBST(root.right, root.data, max)
        
        def sizeOfBST(root):
            if not root: return 0
            return sizeOfBST(root.left) + 1 + sizeOfBST(root.right)
        
        if isBST(root, float("-inf"), float("inf")):
            return sizeOfBST(root)
        return max(self.largestBst(root.left), self.largestBst(root.right))

# Time Complexity = O(N * N) ; as starting from root everytime
# Space Complexity = O(1)    ; as not using any extra data-stracture 
'''

# Method - 2
class Solution:
    def largestBst(self, root):
        def solveLargestBST(root):
            if not root: return (float("-inf"), float("inf"), 0, True)
            if not root.left and not root.right: 
                return (root.data, root.data, 1, True)
            l = solveLargestBST(root.left)
            r = solveLargestBST(root.right)
            
            if l[3] and r[3] and l[1] < root.data < r[0]:
                return (l[0], r[1], 1 + l[2] + r[2], True)
            else:
                return (0, 0, max(l[2], r[2]), False)
            
        ans = solveLargestBST(root)
        return ans[2]