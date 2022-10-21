
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        rootDict = {}
        
        def solve(root, l, d):
            if not root: return
            if d not in rootDict: 
                rootDict[d] = [(l, root.val)]
            else:
                rootDict[d].append((l, root.val))
            solve(root.left, l+1, d-1)
            solve(root.right, l+1, d+1)
        
        solve(root, 0, 0)
        keys = sorted(list(rootDict.keys()))
        
        res = []
        for key in keys:
            arr = sorted(rootDict[key])
            res.append([r[1] for r in arr])
        return res