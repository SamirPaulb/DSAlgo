class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefixSum = 0
        
class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.keyDict = {}

    def insert(self, key: str, val: int) -> None:
        if key in self.keyDict: 
            preVal = self.keyDict[key]
            self.keyDict[key] = val
            val = val - preVal
        else: 
            self.keyDict[key] = val
        cur = self.root
        for c in key:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.prefixSum += val

    def sum(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c not in cur.children: return 0
            cur = cur.children[c]
        return cur.prefixSum

