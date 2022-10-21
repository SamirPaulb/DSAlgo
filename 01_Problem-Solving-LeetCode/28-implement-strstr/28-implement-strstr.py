class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        lh = len(haystack)
        ln = len(needle)
        
        for i in range(lh):
            if needle[0] == haystack[i] and i + ln <= lh:
                if haystack[i:i+ln] == needle:
                    return i
        
        return -1