class Solution:
    def countGoodNumbers(self, n: int) -> int:
        ans = 1
        rem = n % 2
        n -= rem
        ans = pow(20, n//2, 10**9 + 7)
        if rem == 1:
            ans *= 5
        return ans % (10**9 + 7)