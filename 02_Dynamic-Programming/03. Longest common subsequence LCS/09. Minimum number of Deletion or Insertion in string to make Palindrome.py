# https://www.youtube.com/watch?v=CFwCCNbRuLY&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=27
# https://practice.geeksforgeeks.org/problems/minimum-deletitions1648/1#
# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

'''
use LPS => LCS
Minimum number of Deletion or Insertion  in a string to make it a palindrome => Maximum Length of Palindromic Subsequence(LPS) after Deletion or Minimum number of Deletion or Insertion.
numebr of deletion = len(input) - LPS(input)
LPS(X) = LCS(X, X[::-1)
'''
class Solution:
    def minimumNumberOfDeletions(self,S):  #or minInsertions(self, S):
        def LCS(X, Y):
            m = len(X); n = len(Y)
            dp = [[0]*(n+1) for i in range(n+1)]
            # 0th row and 0th coloum initialize as 0; as for size of any of X or Y equal 0 No common subsequence
            for i in range(1, m+1):
                for j in range(1, n+1):
                    if X[i-1] == Y[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            
            return dp[-1][-1]
        
        LPS = LCS(S, S[::-1])
        
        return len(S) - LPS


# For minmum number of deletion, LCS charecters are already palindromic so we have to delete elements which are not palindromic which is epual to len(S) - LCS.    
# For minmum number of insertions LCS charecters are already palindromic so we have to insert same number of non LCS charecters which is equal to len(S) - LCS.
