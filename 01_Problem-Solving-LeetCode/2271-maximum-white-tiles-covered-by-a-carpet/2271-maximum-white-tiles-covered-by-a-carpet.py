class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        ans = 0
        starts, ends = zip(*tiles)
        dp = [0]*(len(tiles) + 1)
        for i in range(len(tiles)):
            dp[i+1] = dp[i] + ends[i] - starts[i] + 1
        for l in range(len(tiles)):
            e = starts[l] + carpetLen
            r = bisect_right(starts, e)
            ans = max(ans, dp[r] - dp[l] - max(0, ends[r-1] - e + 1))
        return ans