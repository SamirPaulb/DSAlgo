# https://leetcode.com/problems/integer-break/

# Method 1 ------  Memoization  -------
# https://youtu.be/in6QbUPMJ3I
class Solution:
    def integerBreak(self, n):
        dp = {1 : 1}
        
        def dfs(num):
            if num in dp:
                return dp[num]
            
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                val = dfs(i) * dfs(num - i)
                dp[num] = max(dp[num], val)
            return dp[num]
        
        return dfs(n)


# Method 2 -------  Dynamic Programming -------
class Solution(object):
    def integerBreak(self, n):
        dp = [None, 1]
        for m in range (2, n + 1):
            j = m - 1
            i = 1
            max_product = 0
            while i <= j:
                max_product = max(max_product, max(i, dp[i]) * max(j, dp[j]))
                j -= 1
                i += 1
            dp.append(max_product)
        return dp[n]
# Time: O(n^2)
# Space: O(n)

# Method 3 ------ Mathematics -------
'''
From the hint:
7 = 3 + 4 = 12
8 = 3 + 3 + 2 = 18
9 = 3 + 3 + 3 = 27
10 = 3 + 3 + 4 = 36
11 = 3 + 3 + 3 + 2 = 54
12 = 3 + 3 + 3 + 3 = 81
Three is a magic number.
'''
class Solution(object):
    def integerBreak(self, n):
        if n == 2 or n == 3:
            return n - 1
        if n % 3 == 0:
            return 3**(n/3)
        if n % 3 == 1:
            return 3**(n/3 - 1)*4
        if n % 3 == 2:
            return 3**(n/3)*2
