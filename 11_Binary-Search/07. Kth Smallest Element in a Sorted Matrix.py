# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row = len(matrix); col = len(matrix[0])
        def isValid(num):  
            count = 1
            for i in range(row):
                l = 0; r = col-1
                while l <= r:     # bisect.bisect_left(matrix[i], num)
                    mid = l + (r - l) // 2
                    if matrix[i][mid] <= num:
                        l = mid + 1
                    else:
                        r = mid - 1
                count += l
            return count <= k
        
        mini = matrix[0][0]; maxi = matrix[0][-1]
        for i in range(row):
            mini = min(mini, matrix[i][0])
            maxi = max(maxi, matrix[i][-1])
            
        l = mini; r = maxi
        while l <= r:
            mid = l + (r - l) // 2
            if isValid(mid):
                l = mid + 1
            else: 
                r = mid - 1
                
        return l
    
    
# Time: O(log(maxi) * row * log(col))
# Space: O(1)
