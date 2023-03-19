# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

    def search(self, word: str) -> bool:
        def dfs(cur, word):
            if not word:
                return cur.isWord
            elif word[0] in cur.children:
                return dfs(cur.children[word[0]], word[1:])
            elif word[0] == '.':
                tmp = False
                for c in cur.children:
                    tmp |= dfs(cur.children[c], word[1:])
                return tmp
            return False
        
        return dfs(self.root, word)
