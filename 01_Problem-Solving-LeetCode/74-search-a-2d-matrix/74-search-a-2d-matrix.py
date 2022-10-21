class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix); n = len(matrix[0])
        
        # Find target Row
        l = 0; r = m-1
        while l <= r:
            mid = (l+r)//2
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                return True
            
        targetRow = r
        
        # search in targetRow
        l = 0; r = n-1
        while l <= r:
            mid = (l+r)//2
            if matrix[targetRow][mid] > target:
                r = mid -1
            elif matrix[targetRow][mid] < target:
                l = mid + 1
            else:
                return True
        
        return False

# Time: O(log(m) + log(n)) = O(log(mn))
# Space: O(1)