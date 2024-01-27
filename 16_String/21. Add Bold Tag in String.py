# https://www.lintcode.com/problem/1127/
# https://leetcode.com/problems/add-bold-tag-in-string/

class Solution:
    def add_bold_tag(self, s: str, dict: List[str]) -> str:
        paint = [False]*len(s)
        for i in range(len(s)):
            for w in dict:
                if i+len(w) <= len(s) and s[i:i+len(w)] == w:
                    paint[i:i+len(w)] = [True] * len(w)
        res = ""
        for i in range(len(s)):
            if paint[i] and (i == 0 or not paint[i-1]):
                res += "<b>"
            res += s[i]
            if paint[i] and (i == len(s)-1 or not paint[i+1]):
                res += "</b>"
        return res


