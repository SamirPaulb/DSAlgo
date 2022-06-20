# https://practice.geeksforgeeks.org/problems/negative-weight-cycle3504/1#
# https://youtu.be/75yC1vbS8S8

# Method 1: Bellman Ford Algorithm
class Solution:
	def isNegativeWeightCycle(self, n, edges):
        dist = [2**31] * n
        dist[0] = 0

        for i in range(n):
            for j in range(len(edges)):
                frm = edges[j][0]
                to = edges[j][1]
                weight = edges[j][2]
                if dist[frm] != 2**31 and dist[frm] + weight < dist[to]:
                    dist[to] = dist[frm] + weight
        
        for j in range(len(edges)):
            frm = edges[j][0]
            to = edges[j][1]
            weight = edges[j][2]
            if dist[frm] != 2**31 and dist[frm] + weight < dist[to]:
                return 1  # True
        
        return 0  # False

		
# Time: O(V * E)
# Space: O(V)
# Where V = number of vertices and E = number of edges



''' 
# Method 2: Dijkstra's Shortest Path Algorithm

class Solution:
    def isNegativeWeightCycle(self, n, edges):
        #Code here
        adjList = {i:[] for i in range(n)}
        for edge in edges:
            adjList[edge[0]].append((edge[2], edge[1])) # (weight. node)
            
        for i in range(n):
            visited = [False] * n
            minHeap = [(0, i)]
            while minHeap:
                dist, node = heapq.heappop(minHeap)
                if visited[node] == True: 
                    if node == i and dist < 0: return 1
                    continue
                visited[node] = True
                for c in adjList[node]:
                    heapq.heappush(minHeap, (dist + c[0], c[1]))
        
        return 0

# Time: O(N * E * log(E))
# Space: O(N * E)
'''