# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
'''
In this we will store each unique lenght substring separetly and will compare with all the possible permutation.
'''


#----------------------- Method 1 -----------------------
class Solution:
    def maxLength(self, arr):
        dp = [set()]  # adding an empty set
        for a in arr:
            if len(set(a)) < len(a): continue  # repeated character is string
            a = set(a)
            for c in dp:
                if a & c: continue # intersection of 2 sets is not empty 
                dp.append(a | c)   # adding union of set a and c
        
        return max(len(a) for a in dp)
    
    
#----------------------- Method 2 -----------------------
class Solution:
    def maxLength(self, arr):
        unique = ['']
        for a in arr:
            for b in unique:
                if len(a+b) == len(set(a+b)):  # a and b are Mutual Exclusivity
                    unique.append(a+b)
        
        return max(len(a) for a in unique)
    
    
#----------------------- Method 3 -----------------------
class Solution:
    def maxLength(self, arr):
        self.res = 0
        def dfs(i, s):
            if len(set(s)) < len(s): 
                return
            self.res = max(self.res, len(s))
            for j in range(i, len(arr)):
                dfs(j+1, s + arr[j])
        
        dfs(0, "")
        return self.res
            
        
        
# Time: O(N^2)  # For All Methods 1, 2, 3
