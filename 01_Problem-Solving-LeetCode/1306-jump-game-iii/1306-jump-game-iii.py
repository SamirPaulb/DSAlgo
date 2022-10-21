class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [False]*len(arr)
        
        def dfs(i):
            if not 0 <= i < len(arr) or visited[i]: return False
            if arr[i] == 0: return True
            visited[i] = True
            return dfs(i-arr[i]) or dfs(i+arr[i])
        
        return dfs(start)