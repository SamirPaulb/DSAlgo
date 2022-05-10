# https://leetcode.com/problems/longest-consecutive-sequence/

''' 
As we have to find the max consecutive length (ie. sorted array) so start from the smallest value (ie. the 
element where num-1 not present) then keep counting greater consecutive elements.

Instead of using 2 loops we basically traversed each element only once. So it is Linear Time. 
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        track = set(nums)
        res = 0
        
        for num in nums:
            if (num - 1) not in track:
                tmpRes = 1
                while (num + 1) in track:
                    tmpRes += 1
                    num += 1
                res = max(res, tmpRes)
        
        return res

# Time: O(N)
# Space: O(N)