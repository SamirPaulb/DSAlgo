# https://leetcode.com/problems/max-points-on-a-line/


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 1
        for i in range(len(points)):
            slopDict = {}
            for j in range(len(points)):
                if i == j: continue
                elif points[i][0] == points[j][0]:
                    if "inf" not in slopDict: slopDict["inf"] = 2
                    else: slopDict["inf"] += 1
                else:
                    slop = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                    if slop not in slopDict: slopDict[slop] = 2
                    else: slopDict[slop] += 1
                        
            if slopDict: res = max(res, max(slopDict.values()))
        
        return res
