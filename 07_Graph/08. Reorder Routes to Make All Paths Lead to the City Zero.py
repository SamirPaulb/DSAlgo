# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = {i:set() for i in range(n)}
        directedAdj = {i:set() for i in range(n)}
        
        for a, b in connections:
            adj[a].add(b)
            adj[b].add(a)
            directedAdj[a].add(b)
        
        visited = {i:False for i in range(n)}
        q = collections.deque([0])
        res = 0
        while q:
            a = q.popleft()
            visited[a] = True
            for b in adj[a]:
                if not visited[b]:
                    if b in directedAdj[a]:
                        res += 1
                    q.append(b)
        
        return res
