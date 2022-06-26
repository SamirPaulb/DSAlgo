# https://leetcode.com/problems/count-number-of-ways-to-place-houses/

'''
One side of street has no effect to the other. The number of way on one side is fibo sequence.
return fibo * fibo in the end.
'''
class Solution:
    def countHousePlacements(self, n):
        a, b, mod = 1, 1, 10**9 + 7
        for i in range(n):
            a, b = b, (a + b) % mod
        return b * b % mod
'''
Time O(n)
Space O(1)
'''


class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [1, 1] 
        for i in range(2, n + 2) :
            dp.append(dp[i-1] + dp[i-2])
        return (dp[n+1] ** 2) % MOD
'''
Time O(n)
Space O(n)
'''
