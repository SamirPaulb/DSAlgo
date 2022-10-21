class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        print(points)
        arrow = points[0][1]
        res = 1
        for p in points[1:]:
            if p[0] > arrow:
                res += 1
                arrow = p[1]
        
        return res