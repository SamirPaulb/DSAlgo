class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        countDict = {}
        for i in nums:
            if i not in countDict: countDict[i] = 1
            else: countDict[i] += 1
        
        res = 0
        for i in countDict:
            if k == 0:
                if countDict[i] > 1: res += 1
            else:
                if k + i in countDict:
                    res += 1
        
        return res