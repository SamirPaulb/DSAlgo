# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        res = 0
        dic = { "I" : 1,
                "IV": 4,
                "V" : 5,
                "IX": 9,
                "X" : 10,
                "XL": 40,
                "L" : 50,
                "XC": 90,
                "C" : 100,
                "CD": 400,
                "D" : 500,
                "CM": 900,
                "M" : 1000,
                }
        
        i = 0
        while i < n:
            if i < n-1 and s[i:i+2] in dic:
                res += dic[s[i:i+2]]
                i += 2
            else:
                res += dic[s[i:i+1]]
                i += 1
        
        return res

# Time: O(N)
# Space: o(N)