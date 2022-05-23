# https://leetcode.com/problems/redundant-connection/
# https://youtu.be/Cb6p18e9c8s

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {i:i for i in range(1, n+1)}
        
        def find(node):
            while parent[node] != node:
                node = parent[node]
            return node
        
        def union(i, j):
            iRoot = find(i)
            jRoot = find(j)
            parent[jRoot] = parent[iRoot]
            
        for edge in edges:
            if find(edge[0]) == find(edge[1]): return edge
            union(edge[0], edge[1])
        
        
# Time: O(N)  ;as the while loop in find() function will run at max 2 time
# Space: O(N)  ;as for taking parent dictionary