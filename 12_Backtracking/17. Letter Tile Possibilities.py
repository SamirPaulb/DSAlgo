# https://leetcode.com/problems/letter-tile-possibilities/

# Broute Force
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        def dfs(path, tiles):
            if path:
                res.add(path)
            for i in range(len(tiles)):
                dfs(path + tiles[i], tiles[:i] + tiles[i+1:])
        
        dfs("", tiles)
        return len(res)
    
    
# Optimal Solution
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        record = [0] * 26
        for tile in tiles: record[ord(tile)-ord('A')] += 1
        def dfs(record):
            s = 0
            for i in range(26):
                if not record[i]: continue
                record[i] -= 1
                s += dfs(record) + 1 
                record[i] += 1
            return s    
        return dfs(record)

# Time: O(n)
# Space: O(n)
