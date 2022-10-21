class Solution:
    def numSplits(self, s: str) -> int:
        left = [0]*len(s)
        right = [0]*len(s)
        
        keep = set()
        count = 0
        for i, ch in enumerate(s):
            if ch not in keep:
                count += 1
            keep.add(ch)
            left[i] = count
        
        keep = set()
        count = 0
        for i in range(len(s)-1, -1, -1):
            right[i] = count
            if s[i] not in keep:
                count += 1
            keep.add(s[i])
            
        res = 0
        for i in range(len(s)):
            if left[i] == right[i]:
                res += 1
                
        return res