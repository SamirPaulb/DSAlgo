# https://www.codingninjas.com/codestudio/problems/implement-trie_1387095

# https://youtu.be/ict1UawpXMM?t=359

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWordCount = 0
        self.prefixOfWordCount = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.prefixOfWordCount += 1
        cur.endOfWordCount += 1

    def countWordsEqualTo(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        return cur.endOfWordCount

    def countWordsStartingWith(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        return cur.prefixOfWordCount

    def erase(self, word):  # Dele te function
        cur = self.root
        toBeDeleted = None
        for c in word:  # as it a delete function so word is present in trie so we don't need to check if key 'c' present in children hashmap or not. 
            cur = cur.children[c]
            cur.prefixOfWordCount -= 1
            if toBeDeleted:
                toBeDeleted = None
            if cur.prefixOfWordCount == 0:
                toBeDeleted = cur
                
        if toBeDeleted:
            toBeDeleted = None
        cur.endOfWordCount -= 1
        
        
    # It will also work if we don't delete the node only decrease the counts
    def erase(self, word):  # Dele te function
        cur = self.root
        for c in word:  # as it a delete function so word is present in trie so we don't need to check if key 'c' present in children hashmap or not. 
            cur = cur.children[c]
            cur.prefixOfWordCount -= 1
                
        cur.endOfWordCount -= 1