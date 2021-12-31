# https://www.youtube.com/watch?v=SqA0o-DGmEw&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=40
# https://leetcode.com/problems/scramble-string/

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        mp = {} # hash map to store calculated values of solve(a, b) substrings for future use or can take dp matrix to store
        def solve(a, b):
            if len(a) != len(b): return False # if length is not equal then can not be compared with each-other or not scrambled
            
            if a == b: return True  # equal substrungs are already scrambled
            if len(a) <= 1 or len(b) <= 1: return False  # if length == 0 => can not be scrambled; if length == 1 then both should a == b which is checked earlier 
            
            # Check for the condition of anagram
            if sorted(a) != sorted(b): return False
            
            key = a + "-" + b  # key to store value of solve(a, b) in hashmap
            
            if key in mp: return mp[key] # if key present in hashmap ie. previously solve(a, b) was calculated so don't need to calculate again return from here
            
            flag = False
            
            n = len(a)
            
            for i in range(1, n):
                
                noswap = solve(a[:i], b[:i]) and solve(a[i:], b[i:])   # checking left half of a with left half of b AND right half of a with right half of b
                
                swap = solve(a[:i], b[n-i:]) and solve(a[i:], b[:n-i]) # checking left half of a with right half of b AND right half of a with left half of b
                
                if noswap or swap:  # if any one of conditions == True
                    flag = True
                    break
                
            mp[key] = flag  # storing value of solve(a, b) in hashmap
            return mp[key]  # returning value of solve(a, b)
        
        return solve(s1, s2)
    
'''
Time Complexity: O(N^2), where N is the length of the given strings.
Auxiliary Space: O(N^2), As we need to store O(N^2) string in our mp map.

'''               