# https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        preEnd = intervals[0][1]
        # print(intervals)
        for cur in intervals[1:]:
            curStart = cur[0]
            curEnd = cur[1]
            if curStart < preEnd:
                preEnd = min(preEnd, curEnd)
                res += 1
            else:
                preEnd = curEnd
        
        return res
      
      
# Time: O(N log(N))
# Space: O(1)
