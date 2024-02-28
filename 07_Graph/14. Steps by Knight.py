# https://www.geeksforgeeks.org/problems/steps-by-knight5927/1

import collections

class Solution:
	def minStepToReachTarget(self, KnightPos, TargetPos, N):
		q = collections.deque()
        q.append((KnightPos[0]-1, KnightPos[1]-1, 0))
        visited = [[False]*N for _ in range(N)]
        visited[KnightPos[0]-1][KnightPos[1]-1] = True
        moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        
        while q:
            i,j,steps = q.popleft()
            if i == TargetPos[0]-1 and j == TargetPos[1]-1: return steps
            for dx,dy in moves:
                x,y = i+dx,j+dy
                if 0<=x<N and 0<=y<N and not visited[x][y]:
                    q.append((x,y,steps+1))
                    visited[x][y] = True
        
        return -1
            
        
# Time: O(N^2)
# Space: O(N^2)
