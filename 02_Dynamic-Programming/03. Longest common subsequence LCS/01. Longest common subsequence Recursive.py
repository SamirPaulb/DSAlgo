'''
https://www.youtube.com/watch?v=4Urd0a0BNng&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=20
https://leetcode.com/problems/longest-common-subsequence/
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        X = text1; Y = text2; n = len(text1); m = len(text2)
        def LCS(X, Y, n, m):
            # base condition (if one of the string string length is zero we just have to return zero)
            if n == 0 or m == 0:
                return 0
            
            # success condition if the character at last of both string match then we just have to decrement length of both strings
            if X[n - 1] == Y[m - 1]: 
                return 1 + LCS(X, Y, n-1, m-1)
            
             # success condition if the character at last of both string match then we just have to decrement length of either of string
            else:
                return max(LCS(X, Y, n-1, m), LCS(X, Y, n, m-1))
        
        return LCS(X, Y, n, m)


''' 
But this approach will give you (Time Limit Exceeded) error for

s = Solution()
print s.longestCommonSubsequence("ylqpejqbalahwr", "yrkzavgdmdgtqpg")
'''

