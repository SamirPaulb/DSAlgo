class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row = len(image); col = len(image[0])
        visited = [[False]*(col) for i in range(row)]
        val = image[sr][sc]
        q = collections.deque()
        q.append((sr, sc))
        
        while q:
            r, c = q.pop()
            if not 0<= r < row or not 0<= c< col or visited[r][c] == True or image[r][c] != val: continue
            visited[r][c] = True
            image[r][c] = newColor
            q.append((r-1, c))
            q.append((r+1, c))
            q.append((r, c-1))
            q.append((r, c+1))
        
        return image