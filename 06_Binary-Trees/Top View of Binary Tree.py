# https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1#

class Solution:
    def topView(self,root):
        distanceDic = {}
        q = []
        
        if not root: return q
        q.append([root, 0]) # Elements of q is [Node, Horizontal distance of that node from root]
        
        while q:
            tmp = q.pop(0)
            node = tmp[0]
            dis = tmp[1]
            if dis not in distanceDic: 
                distanceDic[dis] = node.data
            if node.left: q.append([node.left, dis - 1])
            if node.right: q.append([node.right, dis + 1])
        
        distanceDicKeys = list(distanceDic.keys())
        distanceDicKeys.sort()
        
        ans = []
        for i in distanceDicKeys:
            ans.append(distanceDic[i])
        
        return ans
        
