# https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/

class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        return s == target or (int(s, 2) > 0 and int(target, 2) > 0)
        
        
# Time complexity: O(n)
