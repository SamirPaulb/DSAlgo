class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sumDic = {0:-1}
        curSum = 0
        res = 0
        
        for i, ch in enumerate(nums):
            if ch == 1: curSum += 1
            else: curSum -= 1
            
            if curSum not in sumDic:
                sumDic[curSum] = i
            else:
                res = max(res, i - sumDic[curSum])
        
        return res