class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        n = len(s); k = len(p)
        if n < k: return res
        
        pDic = {chr(97+i):0 for i in range(26)}
        for i in p:
            pDic[i] += 1
        
        sDic = {chr(97+i):0 for i in range(26)}
        for i in s[:k]:
            sDic[i] += 1

        i = 0
        while i < n-k+1:
            if sDic == pDic:
                res.append(i)
            if i == n-k: break
            sDic[s[i+k]] += 1
            sDic[s[i]] -= 1
            i += 1
        
        return res