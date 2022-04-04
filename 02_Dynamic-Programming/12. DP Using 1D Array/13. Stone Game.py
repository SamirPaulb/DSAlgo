# https://leetcode.com/problems/stone-game/
# https://youtu.be/uhgdXOlGYqE
'''
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # as sum(piles) is odd and Alice always choose first so there is always an way
        that Alice will win
        return True
        
'''

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        
        def dfs(l, r):
            if l > r: return 0
            
            if (l, r) in dp: return dp[(l, r)]
            
            even = True if (r - l) % 2 == 0 else False
            
            left = piles[l] if even else 0
            right = piles[r] if even else 0
            
            dp[(l, r)] = max(left + dfs(l+1, r), right + dfs(l, r-1))
            
            return dp[(l, r)]
        
        return dfs(0, len(piles)-1) > sum(piles) // 2