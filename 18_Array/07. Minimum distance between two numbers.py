# https://practice.geeksforgeeks.org/problems/minimum-distance-between-two-numbers/1

'''
class Solution:
    def minDist(self, arr, n, x, y):
        res = 2**31
        j = 0
        for i in range(n):
            while arr[i] == x and j < i:
                if arr[j] == y: res = min(res, i - j)
                j += 1
        j = 0
        for i in range(n):
            while arr[i] == y and j < i:
                if arr[j] == x: res = min(res, i - j)
                j += 1

        return res if res != 2**31 else -1
'''

class Solution:
    def minDist(self, arr, n, x, y):
        res = 2**31
        ix = iy = -1
        
        for i in range(n):
            if arr[i] == x: ix = i
            if arr[i] == y: iy = i
            if ix != -1 and iy != -1: res = min(res, abs(ix - iy))
            
        return res if res != 2**31 else -1
      
      
'''
Time Complexity: O(N)
Auxiliary Space: O(1)
'''
