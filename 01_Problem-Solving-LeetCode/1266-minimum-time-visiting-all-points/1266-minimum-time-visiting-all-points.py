class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points)-1):
            res += max(abs(points[i+1][0] - points[i][0]), abs(points[i+1][1] - points[i][1]))
        
        return res