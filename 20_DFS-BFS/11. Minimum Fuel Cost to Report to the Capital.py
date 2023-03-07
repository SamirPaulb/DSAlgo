# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/
# https://youtu.be/I3lnDUIzIG4

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj = defaultdict(list)
        for a, b in roads: adj[a].append(b), adj[b].append(a)
        
        def dfs(node, parent):
            nonlocal res
            passengers = 0
            for child in adj[node]:
                if child != parent:
                    p = dfs(child, node)
                    res += ceil(p / seats)
                    passengers += p
            return passengers + 1
         
        res = 0
        dfs(0, -1)
        return res
    
    
# Time: O(N)
