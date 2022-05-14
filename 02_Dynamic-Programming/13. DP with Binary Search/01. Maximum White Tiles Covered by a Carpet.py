# https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/

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

''' 
We create a prefix sum array dp to store the TOTAL coverage from index 0 to the beginning of each tile
Then for the start s of each tile, if we use the carpet there, the end index of the carpet will be s + carpetLen. 
We binary search that value to see which tile on the right would the end index belongs to
Finally, knowing the index of the right tile r, we subtract the TOTAL coverage of the right tile to the
TOTAL coverage of the left tile and any offset (since the end index may lie within the right tile, 
or on the right hand side of it if the right tile is the last one)
Runtime: O(nlogn)
'''