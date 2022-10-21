class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0; twos = 0
        
        for num in nums:
            ones = (ones ^ num) & (~ twos)
            twos = (twos ^ num) & (~ ones)
        
        return ones