class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, ch in enumerate(nums):
            n = target - ch
            if n in dic:
                return [dic[n], i]
            dic[ch] = i
        
        