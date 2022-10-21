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