# https://leetcode.com/problems/beautiful-arrangement/

class Solution:
    def countArrangement(self, n):
        arr = [(i+1) for i in range(n)] 
        self.res = 0
        
        def backtrack(arr, i):
            if i == n+1:
                self.res += 1
                return
            for j, ch in enumerate(arr):
                if ch % i == 0 or i % ch == 0:
                    backtrack(arr[:j] + arr[j+1:], i+1)
        
        backtrack(arr, 1)
        return self.res
    

# Time: 2^n ; exponential time as for each element 2 possibility either take or not take. and if take then call further n-1 calls and 2 choise for each call
# Space: O(n)