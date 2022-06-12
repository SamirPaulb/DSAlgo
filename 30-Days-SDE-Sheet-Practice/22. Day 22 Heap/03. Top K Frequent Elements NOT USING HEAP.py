# https://leetcode.com/problems/top-k-frequent-elements/
# https://youtu.be/YPTqKIgVk-k
# Bucket Sort

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = [1,1,1,2,2,3]; k = 2
        numCountDict = {}  # key = num; value = count
        for num in nums:
            if num not in numCountDict: numCountDict[num] = 1
            else: numCountDict[num] += 1
        # numCountDict = {1:3, 2:2, 3:1}
        maxCount = max(numCountDict.values()) # 3
        
        countNumDict = {i:[] for i in range(1, maxCount+1)} # key = count; value = [num,...]
        
        for num in numCountDict:
            countNumDict[numCountDict[num]].append(num)
        # countNumDict = [3:[1], 2:[2], 1:[3]]
        res = []
        for count in range(maxCount, 0, -1):  # count = 3, 2, 1
            if len(res) >= k: break
            if len(countNumDict[count]) > 0:
                res += countNumDict[count]
        
        return res
    
# Time: O(N)
# SPace: O(N)