# https://www.lintcode.com/problem/514
# https://www.youtube.com/watch?v=5eFh5CC-8KY

class Solution:
    def num_ways(self, n: int, k: int) -> int:
        memo = {}

        def solve(n):
            if n == 0: return 0
            if n == 1: return k 
            if n == 2: return k + k*(k-1)
            if k == 1: return 0
            if n in memo: return memo[n]
            memo[n] = solve(n-2)*(k-1) + solve(n-1)*(k-1)
            return memo[n]

        return solve(n)

# Time: without memoization/dp: (n-2)^k ; with memoization/dp: O(n)
# Space: O(n)
