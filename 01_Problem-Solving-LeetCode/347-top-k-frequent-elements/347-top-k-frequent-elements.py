# https://youtu.be/YPTqKIgVk-k
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort
        countDict = {}
        for i in  nums:
            if i not in countDict:
                countDict[i] = 1
            else:
                countDict[i] += 1
                
        n = max(list(countDict.values()))
        dic = {i:[] for i in range(1, n+1)}
        for i in countDict:
            dic[countDict[i]].append(i)
        
        res = []
        for i in range(n, 0, -1):
            if len(dic[i]) > 0:
                res += dic[i]
            if len(res) >= k: 
                break
        return res
    
# Time: O(N)
# Space: O(N)