class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ds = {}
        for i in s:
            if i not in ds:
                ds[i] = 1
            else:
                ds[i] += 1
        
        dt = {}
        for i in t:
            if i not in dt:
                dt[i] = 1
            else:
                dt[i] += 1
        
        for i in dt:
            if i not in ds: return i
            else:
                if dt[i] > ds[i]: return i