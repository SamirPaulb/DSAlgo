class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sd = {chr(i):0 for i in range(97, 123)}
        for i in s:
            sd[i] += 1
        
        td = {chr(i):0 for i in range(97, 123)}
        for i in t:
            td[i] += 1
        
        res = 0
        
        for i in sd:
            if td[i] == 0:
                res += sd[i]
            elif sd[i] > td[i]:
                res += sd[i] - td[i]
        
        return res