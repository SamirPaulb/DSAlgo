class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {i:False for i in range(len(rooms))}
        visited[0] = True
        
        q = rooms[0]
        while q:
            cur = q.pop()
            if visited[cur] == True: continue
            visited[cur] = True
            q += rooms[cur]
            
        for i in visited:
            if visited[i] == False: return False
        
        return True