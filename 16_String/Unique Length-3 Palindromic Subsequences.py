# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

'''
Just notice we need to return the count of distinct palindromes having length 3(point to be noticed).
Special thing about these odd length palindromes are that they have first and last character same 
so we only need to check how many unique characters are there between first and last character(this can be done using set)
'''

class Solution:
    def countPalindromicSubsequence(self, s):
        res = 0
        for i in set(s):
            l = s.find(i)   # first occurance
            r = s.rfind(i)  # last occurance
            res += len(set(s[l+1:r]))  # count of unique element in middle
        
        return res
      
      
# Time O(26n)
# Space O(26n)
