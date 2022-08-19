# https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        lastIndex = {ch:i for i, ch in enumerate(s)}
        res = []
        left = -1
        right = 0
        
        for i, ch in enumerate(s):
            right = max(right, lastIndex[ch])
            if i == right:
                res.append(right - left)
                right = i
                left = i
        
        return res
    
    
# Time: O(N)
# Space: O(N)
