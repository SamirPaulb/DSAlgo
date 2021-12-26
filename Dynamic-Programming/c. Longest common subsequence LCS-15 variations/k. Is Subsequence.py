# https://www.youtube.com/watch?v=QVntmksK2es&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=30
# https://leetcode.com/problems/is-subsequence/
# https://practice.geeksforgeeks.org/problems/check-for-subsequence4930/1
'''
if s is subsequence of t then LCS of s and t should be equal to len(s)
as LCS is the length of Longest Common Subsequence
'''     
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s); n = len(t)
        dp = [[0]*(n+1) for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        return dp[-1][-1] == len(s) # or dp[-1][-1] == m

# Time Complexity = O(m * n)
# Space Complexity = O(m * n)


''' 
# BEST OPTIMAL SOLUTION

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sl = list(s)
        tl = list(t)
        i = 0
        while i < len(sl):
            if i == len(tl):
                return False
            if sl[i] == tl[i]:
                i += 1
            else:
                tl.pop(i)
       
        return sl[:] ==  tl[:len(sl)]                 

# Time Complexity = O(m)
# Space Complexity = O(1)

'''