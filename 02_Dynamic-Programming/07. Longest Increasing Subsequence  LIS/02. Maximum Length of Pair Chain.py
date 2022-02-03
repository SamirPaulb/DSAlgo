# https://leetcode.com/problems/maximum-length-of-pair-chain/

# -------------  DP approach  --------------------
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort(key = lambda x:x[0])
        dp = [1]*n
        
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return dp[-1]
    
# Time Complexity: O(n*n)
# Space Complexity: O(n)



# --------------  Greedy approach  -----------------------------
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort(key = lambda x:x[0])
        res = 1
        left = pairs[0]
        
        for i in range(1, n):
            if left[1] < pairs[i][0]:
                res += 1
                left = pairs[i]
            elif left[1] > pairs[i][1]:
                left = pairs[i]
        
        return res

# Time Complexity: O(n log(n))
# Space Complexity: O(1)
