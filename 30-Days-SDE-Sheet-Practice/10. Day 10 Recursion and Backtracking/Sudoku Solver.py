# https://leetcode.com/problems/sudoku-solver/
# https://youtu.be/uyetDh-DyDg

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row = {i:set() for i in range(9)}
        col = {i:set() for i in range(9)}
        box = {}
        # Making sub-boxes
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.': continue
                key = (i//3, j//3)
                if key not in box: box[key] = {board[i][j]}
                else: box[key].add(board[i][j])
        # Adding values to row, col, box
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                box[(i//3, j//3)].add(board[i][j])
                
        def solve(r, c, board):
            if c >= 9: 
                c = 0
                r += 1
            if r >= 9: return board
            if board[r][c] != '.': 
                if solve(r, c+1, board): return True  # checking if the remaining calls can be valid or not
                else: return False   # if remaining calls not valid then this recursive subtree can not be valid
            else:
                for i in range(1, 10):
                    a = str(i)
                    if a in row[r] or a in col[c] or a in box[(r//3, c//3)]: continue
                    row[r].add(a)
                    col[c].add(a)
                    box[(r//3, c//3)].add(a)
                    board[r][c] = a
                    
                    if solve(r, c+1, board): return True  # if remaining recursive sub-tree is valid then return True from here
                    
                    row[r].remove(a)
                    col[c].remove(a)
                    box[(r//3, c//3)].remove(a)
                    board[r][c] = '.'  # the subtree was not valid so it did not return so update current cell as new
                return False  # No subtree was valid 
            
        solve(0, 0, board)
        return board



        


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

