# https://www.lintcode.com/problem/1308


from typing import List

class Solution:
    def get_factors(self, n: int) -> List[List[int]]:
        if n <= 1: 
            return []

        res = []
        i = 2
        while i*i <= n:
            if n%i == 0:
                res.append([i, n//i])
                subres = self.get_factors(n//i)
                for arr in subres:
                    if arr[0] >= i:
                        res.append([i] + arr)
            i += 1

        return res 


# Time: O(sqrt(n) * log(n))    # https://algo.monster/liteproblems/254
# Space: O(m + log(n))         where m is the number of combinations of factors.
