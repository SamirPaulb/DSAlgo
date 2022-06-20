# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/


# Method 1: Floyd Warshall Algorithm (Dynamic Programming)

class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        dist = [[float('inf')]*n for i in range(n)]  # dist matrix for Dynamic Programming
        for f, t, w in edges:
            dist[f][t] = w
            dist[t][f] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i == j:    # distance of itself is 0
                        dist[i][j] = 0
                    else:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])  # formula of DP
                    
        min_reach = n
        res = 0
        for i in range(n):
            i_reach = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    i_reach += 1
            if i_reach <= min_reach:  # incase of equal, return city with max value
                res = i
                min_reach = i_reach
        
        return res
    
# Time: O(N^3)
# Space: O(N^2)




# Method 2: Dijkstra's Algorithm
'''
we can use Dijkstra's Shortest Path Algorithm for each node to find sortest path to each node. 
But time complexity would be O(N^3 log(N)) for using that minHeap
'''