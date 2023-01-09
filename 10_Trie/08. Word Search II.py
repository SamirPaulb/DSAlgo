# https://leetcode.com/problems/word-search-ii/
# https://youtu.be/asbcE9mZz_U
'''
In Brute Force DFS time complexity: O(k * m * n * 4^(m*n)) where k = len(words)
But we can remove the k if we store all the words into a TRIE.
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
        

class Solution:
    def findWords(self, board, words):
        root = TrieNode()
        row = len(board); col = len(board[0])
        res = set()
        for word in words:
            root.addWord(word)
                
        def dfs(r, c, node, word):
            if not 0<=r<row or not 0<=c<col or board[r][c] == "#" or board[r][c] not in node.children:
                return
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.isWord: 
                res.add(word)
                node.isWord = False
            cur = board[r][c]
            board[r][c] = "#"
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                dfs(r+dx, c+dy, node, word)
            board[r][c] = cur
        
        for r in range(row):
            for c in range(col):
                dfs(r, c, root, "")
        
        return res
    
    
# Time: O(m * n * 4^(m*n))
# Space: O(m*n + k)
