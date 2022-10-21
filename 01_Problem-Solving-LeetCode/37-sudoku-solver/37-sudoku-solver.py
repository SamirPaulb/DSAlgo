class Solution:
    def solveSudoku(self, board):
        
        def backtrack(board, i, j):
            if j == 9: i = i+1; j = 0
            if i == 9: return True
            
            if board[i][j] != ".":
                if backtrack(board, i, j+1): return True    # checking if the remaining calls can be valid or not
                else: return False  # if remaining calls not valid then this recursive subtree can not be valid
                
            else:
                for p in range(1, 10):
                    ch = str(p)
                    if self.isValid(board, i, j, ch):
                        board[i][j] = ch
                        if backtrack(board, i, j+1): return True  # if remaining recursive sub-tree is valid then return True from here
                        board[i][j] = "."  # the subtree was not valid so it did not return so update current cell as new
                return False   # No subtree was valid 
        
        backtrack(board, 0, 0)
        return board
    
    
    def isValid(self, board, i, j, ch):
        # check row i
        for c in range(9):
            if board[i][c] == ch: return False
        
        # check column j
        for r in range(9):
            if board[r][j] == ch: return False
        
        # check sub-boxes of the grid
        smr = (i//3) * 3   # SUb-Matrix up-leftmost corner row index
        smc = (j//3) * 3   # Sub-Matrix up-leftmost corner column index
        for r in range(3):
            for c in range(3):
                if board[smr+r][smc+c] == ch: return False
        
        return True
    
    
# Learn Concept: https://youtu.be/uyetDh-DyDg    
    
'''    
Time complexity: O(9^(n*n)). For every unassigned index, there are 9 possible options so the time complexity is O(9^(n*n)). The time complexity remains the same but checking if a number is safe to use is much faster, O(1).
Space Complexity: O(n*n). As in worst case there can be n*n "." so to update them in board we need to use this space.
'''