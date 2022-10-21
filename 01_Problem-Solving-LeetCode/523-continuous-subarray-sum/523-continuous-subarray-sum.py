class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0 : -1}
        curSum = 0
        
        for i, ch in enumerate(nums):
            curSum += ch
            n = curSum % k
            if n not in dic:
                dic[n] = i
            else:
                if (i - dic[n]) >= 2: return True
        
        return False