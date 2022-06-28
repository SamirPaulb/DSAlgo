# https://practice.geeksforgeeks.org/problems/gold-mine-problem2608/1/#

# Method 1: Traversing from top-left to bottom-right corner # Column wise
class Solution:
    def maxGold(self, n, m, M):
        def get(i, j):
            if not 0<=i<n or not 0<=j<m: return 0
            return M[i][j]
        
        res = 0
        for j in range(m):
            for i in range(n):
                if j == 0:
                    res = max(res, M[i][j])
                else:
                    M[i][j] += max(get(i, j-1), get(i-1, j-1), get(i+1, j-1))
                    res = max(res, M[i][j])
                    
        return res
    
    
#Method 2: Traversing from bottom-right most to top-left most corner; same as Method-1 of 02. Maximum path sum in matrix.py
'''
Available Moves from (i, j) for Maximum Profit:
1. diagonally up towards the right => (i-1, j+1)
2. right => (i, j+1)
3. diagonally down towards the right => (i+1, j+1)
'''
# AS IN ALL MOVES WE NEED VALUE OF (j+1) CELL SO WE HAVE TO TRAVERSE COLUMN WISE 
# to find the value of right column the use it to calculate value of left column
class Solution:
    def maxGold(self, n, m, M):
        
        def get(x, y, r, c):   # to get value from Matrix, this if else can be used in loops also
            if x > r or x < 0: return 0
            elif y > c or y < 0: return 0
            else: return M[x][y]
        
        res = 0
        
        if m == 1:  # 1 Single column
            for i in range(n):
                # Can't get value of right column and can't move downward so max of this single column is result
                res = max(res, M[i][0])
            return res
        
        # TRAVERSE COLUMN-WISE 
        # First calculate (m-2)th column from bottom row to top row then same for (m-3)th column and so on
        for j in range(m-2, -1, -1): # can't include right most column as as right most column can't get value of it's right cell
            for i in range(n-1, -1, -1):
                M[i][j] += max( get(i-1,j+1,n-1,m-1),
                                get(i,j+1,n-1,m-1), 
                                get(i+1,j+1,n-1,m-1))
                res = max(res, M[i][j])
            
        return res  # Max Path of all cells in the matrix
        
        
   
# Time Complexity: O(n * m)
# Space Complexity: O(1)  # as we are not taking any new matrix only making changes in the given matrix.
