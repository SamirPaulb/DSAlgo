# https://leetcode.com/problems/reverse-words-in-a-string/

''' 
class Solution:
    def reverseWords(self, s: str) -> str:
        arr = []
        i = len(s) - 1
        while i >= 0:
            if s[i] != ' ':
                tmp = ''
                while i >= 0 and s[i] != ' ':
                    tmp += s[i]
                    i -= 1
                arr.append(tmp[::-1])
            i -= 1
        
        res = ''
        for i in range(len(arr)):
            if i == len(arr)-1:
                res += arr[i]
            else:
                res += arr[i] + ' '
        
        return res
# Time: O(N)
# Space: O(N)
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0; j = i; n = len(s)
        res = ""
        while i < n:
            if s[i] == " ":
                i += 1
            else:
                j = i
                while j < n and s[j] != " ":
                    j += 1
                subStr = s[i:j]
                if res == "":
                    res = subStr
                else:
                    res = subStr + " " + res
                i = j
        
        return res
            
# Time: O(N)
# Space: O(1)