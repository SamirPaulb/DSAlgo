# https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        
        def dfs(path, u):
            if u == len(graph) - 1:
                res.append(path + [u])
            else:
                for i in graph[u]:
                    dfs(path + [u], i)
        
        dfs([], 0)
        return res