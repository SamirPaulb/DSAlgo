# https://leetcode.com/problems/insert-interval/
# Google Interview Question

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        update = False
        if newInterval[0] <= intervals[0][0]:
            intervals = [newInterval] + intervals
            update = True
        
        if newInterval[0] >= intervals[-1][0]:
            intervals = intervals + [newInterval]
            update = True
        
        for i in range(len(intervals)):
            if intervals[i][0] >= newInterval[0]:
                intervals = intervals[:i] + [newInterval] + intervals[i:] 
                update = True
                break
        #print(intervals)
        i = 1
        while i < len(intervals):
            if intervals[i-1][1] >= intervals[i][0]:
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
                intervals.pop(i)
            else:
                i += 1
        
        return intervals
                
'''
Test Cases:
[[1,3],[6,9]]
[2,5]
[[1,2],[3,5],[6,7],[8,10],[12,16]]
[4,8]
[]
[5,7]
[[1,5]]
[6,8]
[[1,5]]
[0,3]
[[3,5],[12,15]]
[6,6]
'''      