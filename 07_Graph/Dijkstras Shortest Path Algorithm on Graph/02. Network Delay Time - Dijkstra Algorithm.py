# https://leetcode.com/problems/network-delay-time/
# https://youtu.be/EaphyqKU4PQ
'''
# Implement Dijktra's Shortest Path Algorithm
'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # create Adjacency List 
        adjList = {i:[] for i in range(1, n+1)}
        for u, v, w in times:
            adjList[u].append((v, w))
        
        minHeap = [(0, k)]  # taking min-heap so that pop() will give node with lowest distance
        t = 0   # total time require
        visited = set()  # to keep a track of visited nodes
        
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)  # w1 = time to reach from source k(weight); n1 = value of node
            if n1 in visited: continue
            visited.add(n1)
            t = max(t, w1)  # as w1 is the total time to reach to n1 from k
            for n2, w2 in adjList[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1 + w2, n2)) # added current time(w1) + time between n1 and n2
        
        # if we can visit all nodes then only return total time t
        return t if len(visited) == n else -1 

# number of edges, e = len(times)
# n = total no. of nodes

# Time: O(e * log(n)) 
# Space: O(n)