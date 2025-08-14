# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/description/

class Solution:
    def mctFromLeafValues(self, arr):
        n = len(arr)

        # Precompute max values for all subarrays [i..j]
        # Only fill upper triangle and diagonal where i <= j
        maxArr = [[0] * n for _ in range(n)]
        for i in range(n):
            maxVal = arr[i]
            for j in range(i, n):  # j >= i ensures only valid subarrays
                maxVal = max(maxVal, arr[j])
                maxArr[i][j] = maxVal
                # No need to fill maxArr[j][i] (i > j) — it's an invalid range

        memo = {}

        def solve(i, j):
            if i == j:
                return 0  # No non-leaf node for a single leaf

            if (i, j) in memo:
                return memo[(i, j)]

            minCost = float('inf')
            for k in range(i, j):
                left = solve(i, k)
                right = solve(k + 1, j)
                rootVal = maxArr[i][k] * maxArr[k + 1][j]
                minCost = min(minCost, left + right + rootVal)

            memo[(i, j)] = minCost
            return minCost

        return solve(0, n - 1)
