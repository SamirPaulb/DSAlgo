# https://www.lintcode.com/problem/803/

from typing import List
from collections import deque

class Solution:
    def shortest_distance(self, grid):
        # Initialize rows `m` and columns `n` based on the grid dimensions
        m, n = len(grid), len(grid[0])
      
        # A queue for breadth-first search
        queue = deque()
      
        # Total number of buildings
        total_buildings = 0
      
        # Data structures to keep count of how many buildings each empty land can reach
        reach_count = [[0] * n for _ in range(m)]
      
        # Data structures to keep track of total distances from each empty land to all buildings
        distance_sum = [[0] * n for _ in range(m)]
      
        # Loop through each cell in the grid
        for i in range(m):
            for j in range(n):
                # If the cell is a building, perform a BFS from this building
                if grid[i][j] == 1:
                    total_buildings += 1
                    queue.append((i, j))
                    level_distance = 0
                    visited = set()
                    while queue:
                        # Increase the distance level by 1 for each level of BFS
                        level_distance += 1
                      
                        # Loop through each cell in the current BFS level
                        for _ in range(len(queue)):
                            r, c = queue.popleft()
                            # Explore the four directions around the current cell
                            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                                x, y = r + dr, c + dc
                                # If the next cell is valid, not visited, and is an empty land
                                if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and (x, y) not in visited:
                                    # Increment the building reach count and add the distance
                                    reach_count[x][y] += 1
                                    distance_sum[x][y] += level_distance
                                  
                                    # Add the cell to the queue and mark it as visited
                                    queue.append((x, y))
                                    visited.add((x, y))
      
        # Set an initial answer as infinity to find the minimum
        answer = float('inf')
      
        # Loop to find the minimum distance of an empty land cell that can reach all buildings
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reach_count[i][j] == total_buildings:
                    answer = min(answer, distance_sum[i][j])
      
        # If no cell can reach all buildings, return -1; otherwise, return the minimum distance
        return -1 if answer == float('inf') else answer



# Time: O((m * n) * (m * n))    # where m is the number of rows and n is the number of columns in the grid. As there could be up to m * n buildings in the worst case.
# Space: O(m * n) 
