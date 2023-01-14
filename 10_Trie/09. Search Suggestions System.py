# https://leetcode.com/problems/search-suggestions-system/

# Method 1: Sorting
class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()
        res = []
        for i, c in enumerate(searchWord):
            products = [p for p in products if len(p) > i and p[i] == c]
            res.append(products[:3])
        
        return res

# Time: O(N log(N)) + O(N * K) ; where N = len(products), K = len(searchWord)


# ----------------------------------------------------------------------------------------
# Method 2: Trie
class Node:
    def __init__(self):
        self.val = ""
        self.children = {}
        self.suggestions  = []

class Trie:
    def __init__(self):
        self.root = Node()
    
    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
            cur.val = c
            if len(cur.suggestions) < 3:
                cur.suggestions.append(word)
    
    def getSuggestions(self, searchWord):
        cur = self.root
        res = []
        for c in searchWord:
            if c in cur.children:
                cur = cur.children[c]
                res.append(cur.suggestions)
            else: 
                break
        res += [[] for i in range(len(searchWord)-len(res))]
        return res
                
class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()
        trie = Trie()
        for word in products:
            trie.addWord(word)
        return trie.getSuggestions(searchWord)

# Time: O(N log(N)) + O(N * K)

    
# ----------------------------------------------------------------------------------------
# Method 3: Trie + DFS
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.val = ""

class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.val = c
        cur.isWord = True
    
    def suggestedProducts(self, products, searchWord):
        products.sort()
        for product in products:
            self.addWord(product)
        
        def dfs(cur, arr, tmp):
            if len(arr) == 3 or not cur: return 
            if cur.isWord: 
                arr.append(tmp)
            for child in cur.children.values():
                dfs(child, arr, tmp+child.val)
        
        cur = self.root
        res = []
        for i, c in enumerate(searchWord):
            if c not in cur.children: 
                break
            cur = cur.children[c]
            arr = []
            dfs(cur, arr, "")
            for j in range(len(arr)):
                arr[j] = searchWord[:i+1] + arr[j]
            res.append(arr)
            
        res += [[] for i in range(len(searchWord) - len(res))]
        return res
    
# Time: O(N log(N)) + O(N * K)
