# https://leetcode.com/problems/word-break-ii/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        dic = {i : [] for i in range(n+1)}
        
        for i in range(n-1, -1, -1):
            for word in wordDict:
                if i+len(word) <= n and s[i:i+len(word)] == word:
                    dic[i].append(word)
        
        if len(dic[0]) == 0: return []
        
        def solve(j, tmp):
            if j >= n: 
                res.append(tmp)
            for i in range(len(dic[j])): 
                solve(j+len(dic[j][i]), tmp + " " + dic[j][i])
        
        res = []
        for i in range(len(dic[0])):
            j = len(dic[0][i])
            tmp = dic[0][i]
            solve(j, tmp)
        
        return res