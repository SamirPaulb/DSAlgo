# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board); n = len(board[0])
        
        def dfs(i, j, board, word):
            if len(word) == 0: return True  # all the letters are checked
            if (not 0 <= i < len(board)) or (not 0 <= j < len(board[0])): return False
            if board[i][j] != word[0]: return False
            tmp = word[0]
            board[i][j] = '#'  # to mark this cell visited for the current call in current copy of board
            res = ( dfs(i+1, j, board, word[1:]) or
                    dfs(i-1, j, board, word[1:]) or
                    dfs(i, j+1, board, word[1:]) or
                    dfs(i, j-1, board, word[1:]) 
                   )
            board[i][j] = tmp   # during backtracking again update to previous value for using in next calls 
            return res
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:  # 0th letter matches so can check for the next lettere
                    if dfs(i, j, board.copy(), word):  # Passing a copy of board as this cells may be usefull in the next call so do not update the main board
                        return True
        
        return False
    

# Time: O(m*n * 4^s) ; where s = len(word), m = no. of rows and n = no. of cols of the word. Since we may end considering every character(m*n) as a start of the word, and from there we have 4 choices to continue to look for the rest of the word (4^s).

# Space: O(m*n) ; as each time of dfs calling we are passing a copy of main board.