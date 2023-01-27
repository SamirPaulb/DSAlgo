# https://leetcode.com/problems/count-vowels-permutation/

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(1, n):
            a, e, i, o, u = e, a+i, a+e+o+u, i+u, a
            # print(a, e, i, o, u)
        return (a + e + i + o + u) % 1000000007
                    
            
            
# Time: O(n)
# Space: O(1)
