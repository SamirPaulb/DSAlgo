# https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1#
'''
arr[] = {0900, 0940, 0950, 1100, 1500, 1800}
dep[] = {0910, 1200, 1120, 1130, 1900, 2000}
'''

class Solution:    
    #Function to find the minimum number of platforms required at the railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        arr.sort()  # {0900, 0940, 0950, 1100, 1500, 1800}
        dep.sort()  # {0910, 1120, 1130, 1200, 1900, 2000}
        
        i = 1
        j = 0

        res = 1
        platformNeeded = 1
        
        while i < len(arr) and j < len(dep):
            if arr[i] <= dep[j]:
                platformNeeded += 1
                i += 1
            else:
                platformNeeded -= 1
                j += 1
            
            res = max(res, platformNeeded)
        
        return res
        

# Time: O(N log(N))
# Space: O(N)
        