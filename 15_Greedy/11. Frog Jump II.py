# https://leetcode.com/problems/frog-jump-ii/

'''
The best approach is always going to be skipping the next stone and going to next stone after that
'''

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        res = abs(stones[1] - stones[0])
        for i in range(len(stones)-2):
            res = max(res, abs(stones[i+2] - stones[i]))
        return res
    
# Time: O(N)
# Space: O(1)
