class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        visited = {}
        def preorder(root, p):
            if not root: return
            parent[root] = p
            visited[root] = False
            p = root
            preorder(root.left, p)
            preorder(root.right, p)
        preorder(root, None)
        
        res = []
        def dfs(root, k):
            if not root or visited[root] == True: return
            if k == 0: res.append(root.val)
            visited[root] = True
            dfs(root.left, k-1)
            dfs(root.right, k-1)
            dfs(parent[root], k-1)
        
        dfs(target, k)
        return res