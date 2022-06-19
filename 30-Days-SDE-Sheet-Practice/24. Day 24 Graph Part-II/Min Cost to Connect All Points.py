# https://leetcode.com/problems/min-cost-to-connect-all-points/
# https://youtu.be/f7JOBJIC-NA

import heapq
class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        # for simplicity, marking the points with a node value from 0 to (n-1)
        adjList = {i:[] for i in range(n)}  # key = curr node, value = (dist, other nodes)
        for i in range(n):
            x1 = points[i][0]; y1 = points[i][1]
            for j in range(i+1, n):
                x2 = points[j][0]; y2 = points[j][1]
                dist = abs(x1 - x2) + abs(y1 - y2)
                # as it is a undirected graph, we need to add both i and j to adjList
                adjList[i].append((dist, j))
                adjList[j].append((dist, i))
        
        # Prim's Algorithm - Minimum Spanning Tree (MST) 
        # (In the Dijkstra's Algorithm if we introduce a visited data structure to 
        # stop cycle in graph then it converts to Prim's Algorithm)
        visited = set()
        res = 0
        minHeap = [(0, 0)]  # (dist, node)
        while len(visited) < n: # until all nodes a visited
            dist, node = heapq.heappop(minHeap)
            if node in visited: continue
            visited.add(node)
            res += dist
            for dn in adjList[node]:  # dn = (dist, node)
                if dn[1] not in visited:
                    heapq.heappush(minHeap, dn)
        
        return res


# V = number of umber of verices and E = numver of Edges in the graph.
# Time: O(V^2) + O((V+E)logV) = O(V^2)
# Space: O(V^2)  In worst cases all connections of undirected graph can be in minheap 