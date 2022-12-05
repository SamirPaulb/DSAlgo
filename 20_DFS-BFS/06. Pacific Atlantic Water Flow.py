# https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights); col = len(heights[0])
        moves = [(-1,0), (1,0), (0,-1), (0,1)]
        p_visited = set()
        a_visited = set()

        def dfs(i, j, visited):
            if not 0<=i<row or not 0<=j<col or (i,j) in visited: return True
            visited.add((i,j))
            for dx, dy in moves:
                r = i + dx
                c = j + dy
                if 0<=r<row and 0<=c<col and (r,c) not in visited and heights[r][c] >= heights[i][j]:
                    dfs(r, c, visited)

        # iterate from left border and right border
        for i in range(row):
            dfs(i, 0, p_visited)
            dfs(i, col-1, a_visited)

        #iterate from up border and bottom border
        for j in range(col):
            dfs(0, j, p_visited)
            dfs(row-1, j, a_visited)
        
        res = []
        for i in range(row):
            for j in range(col):
                if (i,j) in p_visited and (i,j) in a_visited: 
                    res.append([i,j])
        
        return res


# Time: O(N^2)
# Space: O(N^2)
