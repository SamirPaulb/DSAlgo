# https://leetcode.com/problems/remove-covered-intervals/

class Solution:
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key = lambda x:(x[0], -x[1]))
        res = right = 0
        for l, r in intervals:
            res += r > right
            right = max(r, right)
        return res

# Time: O(N)
# Space: O(1)
    

'''
class Solution:
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key = lambda x:(x[0], -x[1]), reverse = True)
        stack = []
        cnt = 0
        for l, r in intervals:
            while stack and l <= stack[-1][0] and stack[-1][1] <= r:
                stack.pop()
                cnt += 1
            stack.append((l,r))
        
        return len(intervals) - cnt
'''
