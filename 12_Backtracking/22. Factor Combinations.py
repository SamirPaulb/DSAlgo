# https://www.lintcode.com/problem/1308


from typing import List

class Solution:
    def get_factors(self, n: int) -> List[List[int]]:
        self.n = n
        res = []
        def solve(n, i, tmp):
            if n == 1:
                res.append(tmp)
                return 
            while i*i <= n:
                if n%i == 0:
                    solve(n//i, i, tmp + [i])
                i += 1
            if n < self.n:
                solve(n//n, n, tmp + [n])
        solve(self.n, 2, [])
        return res


# Time: O(sqrt(n) * log(n))    # https://algo.monster/liteproblems/254
# Space: O(m + log(n))         where m is the number of combinations of factors.
