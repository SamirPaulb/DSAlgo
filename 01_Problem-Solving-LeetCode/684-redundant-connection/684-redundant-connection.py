class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parentDict = {i:i for i in range(len(edges)+1)}
        
        def find(node):
            while node != parentDict[node]:
                node = parentDict[node]
            return node
        
        def union(a, b):
            aRoot = find(a)
            bRoot = find(b)
            if aRoot == bRoot: return [a, b]
            parentDict[bRoot] = aRoot
        
        for a, b in edges:
            if union(a, b): return union(a, b)
        
        return -1