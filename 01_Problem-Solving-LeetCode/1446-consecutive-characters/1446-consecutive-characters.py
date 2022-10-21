class Solution:
    def maxPower(self, s: str) -> int:
        res = tmp = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                tmp += 1
                res = max(res, tmp)
            else:
                tmp = 1
        
        return res