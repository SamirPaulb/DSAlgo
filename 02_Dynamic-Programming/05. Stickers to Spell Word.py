# https://leetcode.com/problems/stickers-to-spell-word/
# https://youtu.be/hsomLb6mUdI

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        targetSet = set(target)
        stickCount = []
        for s in stickers:
            stick = {}
            for i in s:
                if i in targetSet:
                    stick[i] = stick.get(i, 0) + 1
            stickCount.append(stick)
        
        dp = {}
        def dfs(t, stick):
            if t in dp:
                return dp[t]
            res = 1 if stick else 0
            remainT = ""
            for c in t:
                if c in stick and stick[c] > 0:
                    stick[c] -= 1
                else:
                    remainT += c
            
            if remainT:
                used = 2**31
                for stick in stickCount:
                    if remainT[0] not in stick:
                        continue
                    used = min(used, dfs(remainT, stick.copy()))
                dp[remainT] = used
                res += used
            return res
        
        res = dfs(target, {})
        return res if res != 2**31 else -1
            
        
        
# Time: O(2^n)
