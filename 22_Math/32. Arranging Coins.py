# https://leetcode.com/problems/arranging-coins/
# https://samirpaulb.github.io/assets/arranging-coins-leetcode.png

# ---------- MATH - Time: O(1) ----------
class Solution:
    def arrangeCoins(self, n):
        return int((2*n + 1/4)**(1/2) - 1/2)

    
# ---------- BINARY SEARCH - Time: O(log(N)) ----------
class Solution:
    def arrangeCoins(self, n):
        res = 0
        l, r = 0, (n+1)//2
        while l <= r:
            mid = l + (r-l)//2
            if mid*(mid+1)//2 <= n:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res
