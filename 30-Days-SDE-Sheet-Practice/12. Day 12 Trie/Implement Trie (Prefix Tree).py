# https://leetcode.com/problems/implement-trie-prefix-tree/
# https://youtu.be/oobqoCJlHA0

class TrieNode:
    # creating constructor for TrieNode and assigning attributes to TrieNode
    def __init__(self):
        self.children = {}       # storing children in hashset instead of list to have search in constant time
        self.endOfWord = False   # by default saying that current node is not the end of word 

        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()                 # the root of trie with null value
        
    def insert(self, word: str) -> None:
        cur = self.root                        # starting cur pointer from the main root
        for c in word:                         # search for each letter of word
            if c not in cur.children:          # current letter 'c' not in children hashmap
                cur.children[c] = TrieNode()   # then create new trie node with key 'c' and value Null 
            cur = cur.children[c]              # shift the cur pointer to the 'c' child
        cur.endOfWord = True                   # mark the current not as end of the word

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:          # there if no children in hashmap with key 'c'
                return False                   # the word not present in trie
            cur = cur.children[c]              # shift the cur pointer to the 'c' child
        return cur.endOfWord                   # check if actual word ends here or may be the actual word is longer than given word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True                            # all the letters of prefix has been checked so prefix is present
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)