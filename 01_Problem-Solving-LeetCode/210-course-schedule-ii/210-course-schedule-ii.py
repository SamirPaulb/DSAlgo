class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i:[] for i in range(numCourses)}
        for a in prerequisites:
            adjList[a[0]].append(a[1])
        
        outbound = {i:0 for i in range(numCourses)}
        for a in prerequisites:
            outbound[a[1]] += 1
        
        q = []
        for i in outbound:
            if outbound[i] == 0:
                q.append(i)
                
        res = []
        
        while q:
            a = q.pop()
            res.append(a)
            for i in adjList[a]:
                outbound[i] -= 1
                if outbound[i] == 0:
                    q.append(i)
                    
        for i in outbound:
            if outbound[i] != 0: return []
        
        return res[::-1]