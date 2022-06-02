# https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1#

import collections

class Solution:
    def bottomView(self, root):
        distDict = {}
        
        q = collections.deque([(root, 0)])
        while q:
            tmp = q.popleft()
            node = tmp[0]
            dist = tmp[1]
            
            distDict[dist] = node.data
            
            if node.left: q.append((node.left, dist-1))
            if node.right: q.append((node.right, dist+1))
        
        keys = distDict.keys()
        mini = min(keys)
        maxi = max(keys)
        
        res = []
        for key in range(mini, maxi+1):
            if key in distDict:
                res.append(distDict[key])
        
        return res
        
# Time: O(N)
# Space: O(N)

