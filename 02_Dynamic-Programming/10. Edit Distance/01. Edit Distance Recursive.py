# https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        def solve(w1, w2, n, m): 
            # Base Case if any one of w1 or w2 is empty 
            if n == 0 or m == 0: return m or n
            
            elif w1[n-1] == w2[m-1]:
                return solve(w1, w2, n-1, m-1)
            
            else:
                return 1 + min(
                                solve(w1, w2, n-1, m-1),  # Replace
                                solve(w1, w2, n-1, m),    # Delete
                                solve(w1, w2, n, m-1)     # Insert
                                )
        
        return solve(w1, w2, len(w1), len(w2))
    

# Time Limit Exceeded
# We need to use Memoization in this Solution to avoid repetative same calculation of sub-problems
