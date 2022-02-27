# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1  # Traverse from the end of the strings
        j = len(t) - 1 
        # The number of backspaces required till we arrive at a valid character
        bs = 0  # count of backspace for s
        bt = 0  # count of backspace for t
        
        while i >= 0 or j >= 0:
            while i >= 0:  # count bs
                if s[i] == "#":
                    bs += 1
                    i -= 1
                elif bs > 0 and s[i] != "#":
                    bs -= 1
                    i -= 1
                else:
                    break
                    
            while j >= 0:  # count bt
                if t[j] == "#":
                    bt += 1
                    j -= 1
                elif bt > 0 and t[j] != "#":
                    bt -= 1
                    j -= 1
                else:
                    break
            # Also ensure that both the character indices are valid. If it is not valid,  it means that we are comparing a "#" with a valid character.
            if i >= 0 and j < 0: return False
            if i < 0 and j >= 0: return False
            
            if s[i] != t[j]: return False
            
            i -= 1
            j -= 1
        
        
        return True


# Time Complexity: O(N)
# Space Complexity: O(1)