# https://leetcode.com/problems/count-number-of-ways-to-place-houses/

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
