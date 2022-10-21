class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {chr(97+i):0 for i in range(26)}
        dt = {chr(97+i):0 for i in range(26)}
        
        for i in s:
            ds[i] += 1
        
        for i in t:
            dt[i] += 1
        
        return ds == dt