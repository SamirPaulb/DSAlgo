class Solution:
    def freqAlphabets(self, s: str) -> str:
        n = len(s)
        i = 0
        res = ""
        while i < n:
            if i < n-2:
                if s[i+2] == "#":
                    res += chr(96+int(s[i:i+2]))
                    i += 3
                else:
                    res += chr(96+int(s[i]))
                    i += 1
            else:
                res += chr(96+int(s[i]))
                i += 1
        
        return res