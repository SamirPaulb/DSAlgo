class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        if shifts[-1] > 26: shifts[-1] = shifts[-1] % 26
        for i in range(len(shifts)-2, -1, -1):
            shifts[i] += shifts[i+1]
            if shifts[i] > 26:
                shifts[i] = shifts[i] % 26
        
        s = list(s)
        for i in range(len(s)):
            a = ord(s[i]) + shifts[i]
            a = a % 123
            print(a)
            if a < 97:
                s[i] = chr(97 + a)
            else:
                s[i] = chr(a)
        
        return "".join(s)
    