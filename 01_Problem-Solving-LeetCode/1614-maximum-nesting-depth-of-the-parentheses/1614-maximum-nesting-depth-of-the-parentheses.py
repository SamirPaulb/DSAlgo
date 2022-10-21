class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        count = 0
        
        for i in s:
            if i == "(":
                count += 1
            elif i == ")":
                count -= 1
            res = max(res, count)
        
        return res