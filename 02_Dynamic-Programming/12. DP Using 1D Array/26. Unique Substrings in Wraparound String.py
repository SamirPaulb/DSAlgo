# https://leetcode.com/problems/unique-substrings-in-wraparound-string/

from collections import defaultdict

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = defaultdict(int)
        streak = 0
        for i in range(len(p)):
            if (ord(p[i-1]) - 96) % 26 == (ord(p[i]) - 97):
                streak += 1
            else:
                streak = 1
            dp[p[i]] = max(dp[p[i]], streak)
        # print(dp)
        return sum(dp.values())
    
    
    
class Solution(object):
    def findSubstringInWraproundString(self, p):
        p, d, lo = '0'+p, collections.defaultdict(int), 0
        for hi in range(1, len(p)):
            if p[hi-1]+p[hi] not in 'abcdefghijklmnopqrstuvwxyza':
                lo = hi
            d[p[hi]] = max(d[p[hi]], hi+1-lo)
        return sum(d.values())
