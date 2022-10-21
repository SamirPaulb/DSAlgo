class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        res = []
        
        def dfs(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for ch in digitToChar[digits[i]]:
                dfs(i+1, curStr + ch)
            
        dfs(0, "")
        return res if len(digits) != 0 else []

    
# Time: O(n 4^n)
# Space: O(n)