# https://leetcode.com/problems/merge-intervals/
# sort based on the 0th index element value
# check values of two consecutive elements with 2 pointers. if overlapping then change 1st index of 
# 1st pointer with max and pop 2nd pointer
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        l = 0; r = 1
        
        while r < len(intervals):
            if intervals[l][1] >= intervals[r][0]:
                intervals[l][1] = max(intervals[l][1], intervals[r][1])
                intervals.pop(r)
            
            else:
                l = r
                r += 1
        
        return intervals