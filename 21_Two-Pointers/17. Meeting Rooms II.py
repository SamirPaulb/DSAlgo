# https://www.lintcode.com/problem/919
# https://leetcode.com/problems/meeting-rooms-ii/
# https://www.youtube.com/watch?v=FdzJmTCVyJU


from typing import List
from lintcode import Interval

class Solution:
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        s = e = res = 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
            else:
                e += 1
            res = max(res, s-e)
        
        return res


# Time: O(N log N)
# Space: O(N)
