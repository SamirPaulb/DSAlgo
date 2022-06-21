# https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        
        def dfs(i, j):
            if i == 0 or j == 0: return j or i
                        
            if (i,j) in memo:
                return memo[(i,j)]
            
            if word1[i-1] == word2[j-1]:
                ans = dfs(i-1, j-1)
            else: 
                ans = 1 + min(dfs(i, j-1), dfs(i-1, j), dfs(i-1, j-1))
                
            memo[(i,j)] = ans
            return memo[(i,j)]
        
        return dfs(len(word1), len(word2))
