class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i : [] for i in range(numCourses)}
        
        for i in range(len(prerequisites)):
            a = prerequisites[i]
            adjList[a[0]].append(a[1])
        
        outbound = {i:0 for i in range(numCourses)}
        
        for i in range(len(prerequisites)):
            a = prerequisites[i]
            outbound[a[1]] += 1
        
        q = []
        for i in range(numCourses):
            if outbound[i] == 0:
                q.append(i)
        
        while q:
            a = q.pop(0)
            outbound[a] -= 1
            if outbound[a] <= 0:
                q += adjList[a]          
        
        for i in outbound:
            if outbound[i] > 0: return False
        
        return True