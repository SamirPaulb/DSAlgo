# https://www.lintcode.com/problem/645
# https://leetcode.com/problems/find-the-celebrity/description/

"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""

class Solution:
    def findCelebrity(self, n):
        celeb = 0
        for i in range(n):
            if i != celeb and Celebrity.knows(celeb, i):
                celeb = i
        
        for i in range(n):
            if i != celeb and Celebrity.knows(celeb, i):
                return -1
            if i != celeb and not Celebrity.knows(i, celeb):
                return -1
        
        return celeb
