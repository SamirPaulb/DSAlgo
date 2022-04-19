# https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        countDict = {}
        for i in s:
            if i not in countDict:
                countDict[i] = 1
            else:
                countDict[i] += 1
                
        res = []
        i = 0
        while i < len(s):
            targetSum = 0
            track = set()
            j = i
            while j < len(s):
                if s[j] not in track:
                    track.add(s[j])
                    targetSum += countDict[s[j]]
                if j-i+1 == targetSum:
                    res.append(j-i+1)
                    break
                j += 1
            i = j + 1
        
        return res
    
    
# Time: O(N)
# Space: O(N)
