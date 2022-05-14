# https://leetcode.com/problems/maximum-units-on-a-truck/
''' 
As we need to find maximum counts so that sort the array in decreasing order so that higher 
count per box remain first. Then keep adding and reducing the value of given size.
'''

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x:x[1], reverse = True)
        res = 0
        i = 0
        while i < len(boxTypes):
            if truckSize > boxTypes[i][0]:
                res += boxTypes[i][0] * boxTypes[i][1]
                truckSize -= boxTypes[i][0]
            else:
                res += truckSize * boxTypes[i][1]
                break
            i += 1
        
        return res

# Time: O(N log(N))
# Space: O(1)