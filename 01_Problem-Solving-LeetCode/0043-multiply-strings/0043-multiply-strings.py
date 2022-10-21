class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'
        def decode(s):
            ansInt = 0
            for i in s:
                ansInt = ansInt * 10 + (ord(i) - ord('0')) 
            return ansInt
        
        def encode(s):
            ansStr = ''
            while s:
                ansStr = chr(ord('0') + s % 10) + ansStr
                s = s // 10     
            return ansStr
        
        return encode(decode(num1) * decode(num2))