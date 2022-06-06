# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []
        def inorder(root):
            if not root: return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        
        inorder(root)
        
        l = 0
        r = len(arr)-1
        while l < r:
            twoSum = arr[l] + arr[r]
            if twoSum < k:
                l += 1
            elif twoSum > k:
                r -= 1
            else:
                return True
            
        return False


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited = set()
        self.res = False
        
        def inorder(root):
            if not root: return
            inorder(root.left)
            rem = k - root.val
            if rem in visited: self.res = True
            visited.add(root.val)
            inorder(root.right)
        
        inorder(root)
        return self.res


# Time: O(N)
# Space: O(N)


