# https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1: 
            return ""
        len1, len2 = len(str1), len(str2)
        
        def gcd(a, b):
            if b == 0: return a
            return gcd(b, a%b)
        
        i = gcd(len1, len2)
        return str1[:i]

# Time: O(N) 
# GCD calculation takes O(log(N)) time. But the string iteration and equals checking takes O(N+M) time where, N and M are the length of str1 and str2.



'''
class Solution:
    def gcdOfStrings(self, str1, str2):
        len1, len2 = len(str1), len(str2)
        
        def isDivisor(i):
            if len1 % i or len2 % i:
                return False
            f1, f2 = len1 // i, len2 // i
            return str1[:i] * f1 == str1 and str1[:i] * f2 == str2
        
        for i in range(min(len1, len2), 0, -1):
            if isDivisor(i):
                return str1[:i]
        
        return ""
    
# Time: O(N^2)  # as time to take a substring is O(N)
'''
