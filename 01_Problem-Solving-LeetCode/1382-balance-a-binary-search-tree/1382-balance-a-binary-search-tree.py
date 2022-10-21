class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def inorder(root):
            if not root: return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        
        inorder(root)
        
        def solve(l, r):
            if l > r: return None
            mid = (l + r) // 2
            root = TreeNode(arr[mid])
            root.left = solve(l, mid-1)
            root.right = solve(mid+1, r)
            return root
        print(arr)
        return solve(0, len(arr)-1)