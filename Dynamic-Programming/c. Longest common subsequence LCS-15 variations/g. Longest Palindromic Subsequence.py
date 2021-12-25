# https://www.youtube.com/watch?v=wuOOOATz_IA&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=26
# https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # This LPS can be solved using LCS(Longest Common Subsequence)
        '''
        X = s
        Y = reverse(s)
        Now LCS(X, Y) is the LPS(Longest Palindromic Subsequence)
        s = "agbcba"
        => X = "agbcba"
        => Y = s[::-1] = "abcbga"
        => LCS(X, Y) = "abcba" => which is the longest possible Palindromic Subsequence
        => LPS(s) == LCS(s, s[::-1])
        '''
        def LCS(X, Y):
            m = len(X); n = len(Y)
            dp = [[0]*(n+1) for i in range(m+1)]
            # 0th row and 0th coloum initialize as 0; as for size of any of X or Y equal 0 No common subsequence
            for i in range(1, m+1):
                for j in range(1, n+1):
                    if X[i-1] == Y[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                        
            return dp[-1][-1]
        
        X = s
        Y = s[::-1]
        return LCS(X, Y)
        