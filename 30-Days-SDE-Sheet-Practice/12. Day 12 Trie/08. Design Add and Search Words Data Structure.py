# https://leetcode.com/problems/design-add-and-search-words-data-structure/

# DFS
class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class WordDictionary:
    
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        self.res = False
        self.dfs(self.root, word)
        return self.res
                          
    def dfs(self, node, word):
        if not word:
            if node.endOfWord:
                self.res = True
            return
        
        if word[0] == '.':
            for childNode in node.children.values():
                self.dfs(childNode, word[1:])
            return
                
        else:
            if word[0] in node.children:
                self.dfs(node.children[word[0]], word[1:])
            return



# DFS
class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class WordDictionary:
    
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word)
        
    def dfs(self, node, word):
        if not word:
            return node.endOfWord
        for i in range(len(word)):
            if word[i] == '.':
                for child in node.children.values():
                    if child and self.dfs(child, word[i+1:]): return True
                else: return False
            if word[i] not in node.children:
                return False
            else:
                node = node.children[word[i]]
        return node.endOfWord