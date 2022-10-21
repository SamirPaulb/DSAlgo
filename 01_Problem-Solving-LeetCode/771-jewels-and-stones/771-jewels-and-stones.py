class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        res = 0
        
        for s in stones:
            if s in jewels: res += 1
        
        return res