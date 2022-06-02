# https://www.interviewbit.com/problems/path-to-given-node/

class Solution:
    def solve(self, A, B):
        self.res = []

        def preorder(root, target, path):
            if not root: return
            if root.val == target:
                path += [root.val]
                self.res = path
                return
            preorder(root.left, target, path + [root.val])
            preorder(root.right, target, path + [root.val])
        
        preorder(A, B, [])
        return self.res

# Time: O(N)
# Space: O(1)