# https://leetcode.com/problems/jump-game-iii/

# --------------------------  DFS Approach  -------------------------------
class Solution:
    def canReach(self, arr, start):
        seen = set()

        def dfs(n):
            if n in seen: return False
            if not 0 <= n < len(arr): return False
            if arr[n] == 0: return True
            seen.add(n)
            return dfs(n - arr[n]) or dfs(n + arr[n])
            
        return dfs(start)

# Time O(N); as traversing evry element only once
# Space: O(N)


# --------------------------  BFS Approach  -------------------------------
class Solution:
    def canReach(self, arr, start):
        q = [start]
        visited = [False]*len(arr)

        while q:
            tmp = q.pop()
            if arr[tmp] == 0: return True
            visited[tmp] = True
            r, l = tmp + arr[tmp], tmp - arr[tmp]
            if  r < len(arr) and visited[r] == False:
                q.append(r)
            if l >= 0 and visited[l] == False:
                q.append(l)
                
        return False

# Time O(N); as traversing evry element only once
# Space: O(N)