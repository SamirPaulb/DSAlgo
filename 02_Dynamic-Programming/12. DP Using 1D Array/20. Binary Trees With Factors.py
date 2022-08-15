# https://leetcode.com/problems/binary-trees-with-factors/
# Explanation: https://raw.githubusercontent.com/SamirPaulb/assets/main/823-Binary-Trees-With-Factors_explanation.png

'''
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        countDict = {ch:1 for ch in arr}
        res = 0
        for i in range(len(arr)):
            l, r = 0, i-1
            tmp = countDict[arr[i]]
            while l <= r:
                p = arr[l] * arr[r]
                if p > arr[i]:
                    r -= 1
                elif p < arr[i]:
                    l += 1
                else:
                    if arr[l] != arr[r]: 
                        tmp += 2 * countDict[arr[l]] * countDict[arr[r]]
                    else:
                        tmp += countDict[arr[l]] * countDict[arr[r]]
                    l += 1
                    r -= 1
                    
            countDict[arr[i]] = tmp
            res += tmp
            res = res % (10**9 + 7)
        
        return res
    
# Time: O(N^2)
# Space: O(N)
'''


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        MOD = 10**9 + 7
        dp = {}
        for i, ch in enumerate(arr):
            dp[ch] = 1
            for j in range(i):
                if ch % arr[j] == 0 and (ch // arr[j]) in dp:
                    dp[ch] += dp[arr[j]] * dp[ch // arr[j]]
                    dp[ch] %= MOD
        
        return sum(dp.values()) % MOD
    
# Time: O(N^2)
# Space: O(N)
