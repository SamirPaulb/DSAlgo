# https://leetcode.com/problems/map-sum-pairs/
'''
When you see word prefix in problem formulation, you should definitely think about trie. What we need here is classical trie with one additional field: freq - frequency of each node. For example when we add word apple with val = 3 we need to add this 3 to all a, p, p, l, e nodes. Also we need to deal with this phrase: If the key already existed, the original key-value pair will be overridden to the new one, so we need to keep dictionary of pairs key - value to underastand if they already exist in our tree. Then we evaluate delta = val - self.dic.get(key, 0) is amount we need to change our values. For sum function we find node in our tree and if it is not there, return 0, if we can reach it, return frequency of this node.
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefixCount = 0
        
        
class MapSum:  

    def __init__(self):
        self.root = TrieNode()
        self.dic = {}

    def insert(self, key: str, val: int) -> None: 
        delta = val
        if key in self.dic:     # key already existed, the original key-value pair will be overridden to the new one. And val - self.dic[key] does this thing
            delta = val - self.dic[key]
        self.dic[key] = val
        cur = self.root
        for c in key:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.prefixCount += delta

    def sum(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        return cur.prefixCount

'''
Time complexity: O(m) to insert key of length m as well it is O(m) to evaluate sum for prefix of length m. 
Space complexity: O(T) where T it total length of all words.
'''
