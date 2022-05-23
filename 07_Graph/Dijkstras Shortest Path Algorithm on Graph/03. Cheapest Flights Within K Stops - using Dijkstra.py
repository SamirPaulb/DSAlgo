# https://leetcode.com/problems/cheapest-flights-within-k-stops/
''' 
First Solve => 02. Network Delay Time - using Dijkstra Algorithm
'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #Make graph
        adj_list = {i:[] for i in range(n)}
        for frm, to, price in flights:
            adj_list[frm].append((to, price))
        
        best_visited = [2**31]*n # Initialized to maximum
        
        prior_queue = [ (0, -1, src) ]  # weight, steps, node

        while prior_queue:
            cost, steps, node = heapq.heappop(prior_queue)
            
            if best_visited[node] <= steps:  # Have seen the node already, and the current steps are more than last time
                continue

            if steps > k:  # More than k stops, invalid
                continue

            if node==dst:  # reach the destination # as priority_queue is a minHeap so this cost is the most minimum cost.
                return cost
            
            best_visited[node] = steps # Update steps

            for neighb, weight in adj_list[node]:
                heapq.heappush(prior_queue, (cost + weight, steps + 1, neighb))

        return -1

# Time: O(n * len(flights) * log(n))
# Space: O(n)