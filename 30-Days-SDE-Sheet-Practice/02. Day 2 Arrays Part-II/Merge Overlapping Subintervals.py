# https://leetcode.com/problems/merge-intervals/

# check values of two consecutive elements with 2 pointers
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