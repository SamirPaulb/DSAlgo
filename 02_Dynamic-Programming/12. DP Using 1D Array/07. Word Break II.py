# https://leetcode.com/problems/word-break-ii/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dic = {i : [] for i in range(len(s))}
        
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    dic[i].append(word)
        
        res = []
        if not dic[0]: return res
        
        def solve(i, path):
            if i >= len(s):
                res.append(path)
                return
            for num in dic[i]:
                if path == "":
                    solve(i + len(num), num)
                else:
                    solve(i + len(num), path + " " + num)
        
        solve(0, "")
        return res
