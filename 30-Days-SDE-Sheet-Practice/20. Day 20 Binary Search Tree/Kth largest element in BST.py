# https://practice.geeksforgeeks.org/problems/kth-largest-element-in-bst/1#

class Solution:
    def kthLargest(self,root, k):
        #your code here
        self.k = k
        self.res = root.data
        def reverseInorder(root):
            if not root: return
            reverseInorder(root.right)
            self.k -= 1
            if self.k == 0:
                self.res = root.data
            reverseInorder(root.left)
        
        reverseInorder(root)
        return self.res

# Time: O(N)
# Space: O(1)