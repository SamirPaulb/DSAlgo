class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = {i:[] for i in range(n)}
        for egd in edges:
            a = egd[0]
            b = egd[1]
            adjList[a].append(b)
            adjList[b].append(a)
        
        visited = {i:False for i in range(n)}
        q = [source]
        while q:
            n = len(q)
            for i in range(n):
                node = q.pop()
                if visited[node] == True: continue
                visited[node] = True
                q += adjList[node]
        
        return visited[destination]