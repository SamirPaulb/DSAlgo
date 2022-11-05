# https://practice.geeksforgeeks.org/problems/column-name-from-a-given-column-number4244/1


class Solution:
    def colName (self, n):
        res = ""
        while n > 0:
            i = n % 26
            if i == 0:
                res = 'Z' + res
                n = (n-1)//26
            else:
                res = chr(64 + i) + res
                n = n // 26

        return res
        
'''
Time - O(N)
Space - O(1)
'''
