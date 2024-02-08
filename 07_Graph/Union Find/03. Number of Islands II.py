# https://www.lintcode.com/problem/434
# https://leetcode.com/problems/number-of-islands-ii/

from typing import List
from lintcode import Point
"""
Definition for a point:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
"""

class UnionFind:
    def __init__(self, num):
        self.root = [-1] * num
        self.rank = [0] * num
    def unionByRank(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if i == j:
            return 
        if self.rank[i] < self.rank[j]:
            self.root[i] = j
        elif self.rank[i] > self.rank[j]:
            self.root[j] = i
        else:
            self.root[i] = j
            self.rank[j] += 1
    def find(self, u):
        if self.root[u] != u:
            self.root[u] = self.find(self.root[u])
        return self.root[u]
        
# n = total rows; m = total columns
class Solution:
    def num_islands2(self, n: int, m: int, operators: List[Point]) -> List[int]:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        res = []
        visited = [[False]*m for _ in range(n)]
        uf = UnionFind(n*m)
        count = 0

        def getRoot(i, j):
            return i * m + j
        
        for op in operators:
            i,j = op.x, op.y
            if visited[i][j]:
                res.append(count)
                continue
            visited[i][j] = True
            u = getRoot(i, j)
            uf.root[u] = u 
            count += 1
            for dx,dy in directions:
                r,c = i+dx,j+dy
                if 0<=r<n and 0<=c<m:
                    v = getRoot(r, c)
                    if uf.root[v] == -1: # water
                        continue
                    uRoot = uf.find(u)
                    vRoot = uf.find(v)
                    if uRoot != vRoot:
                        uf.unionByRank(u,v)
                        count -= 1
            res.append(count)
        
        return res


# Time: O(N log(N))
# Space: O(N)
