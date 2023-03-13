# https://leetcode.com/problems/word-break-ii/

# Method-1:  DP + DFS

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

    
    
    
    
# Method-2: DP

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        dp = [[""] for _ in range(n+1)]
        for i in range(1, n+1):
            arr = []
            for word in wordDict:
                if i - len(word) >= 0 and s[i-len(word):i] == word:
                    if i-len(word) == 0:
                        arr.append(word)
                    elif dp[i-len(word)] != [""]:
                        for st in dp[i-len(word)]:
                            arr.append(st + " " + word)
            dp[i] = arr
            
        # print(dp)
        return dp[-1]

    
    
    
    
# Method-3: DP + DFS (Similar to Method-1)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        dp = [[] for _ in range(n+1)]
        for i in range(1, n+1):
            for word in wordDict:
                if i - len(word) >= 0 and s[i-len(word):i] == word:
                    dp[i].append(word)
        
        res = []
        if not dp[-1]: return res
        # print(dp)
        def solve(i, path):
            if i <= 0: 
                res.append(path)
                return
            for st in dp[i]:
                if not path:
                    solve(i-len(st), st)
                else:
                    solve(i-len(st), st + " " + path)
        
        solve(n, "")
        return res
