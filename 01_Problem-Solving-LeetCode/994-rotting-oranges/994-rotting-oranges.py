class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid); col = len(grid[0])
        q = collections.deque()
        fresh_count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1: fresh_count += 1
        
        if fresh_count == 0: return 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        print(q)
        time = 0
        while q:
            n = len(q)
            time += 1
            for _ in range(n):
                i, j = q.popleft()
                for move in directions:
                    r = i + move[0]; c = j + move[1]
                    if 0 <= r < row and 0 <= c < col and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r, c))
                        
        for row in grid:
            if 1 in row: return -1
        return time - 1