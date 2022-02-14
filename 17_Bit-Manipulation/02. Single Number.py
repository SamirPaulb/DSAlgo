# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        (4 XOR 3) XOR 3 = 4
        as xor of same number = 0; so 3^3 = 0; and xor of any number with zero equals that number
        4^3 = 7
        7^3 = 4
        => 4^3^3 = 7
        '''
        res = 0
        for i in nums:
            res = res ^ i  # as twice numbers make them zero and 0 ^ single number = single number
                    
        return res
# Time: O(N)
# Space: O(1)
    
'''
        return 2 * sum(set(nums)) - sum(nums)

Time: O(N)  # as sum() internally use a loop
Space: O(N) # for making set of nums
'''