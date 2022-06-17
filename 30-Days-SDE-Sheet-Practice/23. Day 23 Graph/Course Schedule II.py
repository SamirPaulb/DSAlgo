# https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0 or numCourses == 1: return [0]
        # Making Ajacency List of the Graph
        adjacencyList = {i : [] for i in range(numCourses)} 
        if len(prerequisites) > 0:
            for num in prerequisites:
                adjacencyList[num[0]].append(num[1])
        # BFS
        # outBound = number of elements dependent on the current element => course to be completed before 
        # eg. for [[0,1], [0,2], [1,3], [1,4], [3,4]] outbound of 4 is 2, because 1 and 3 is dependent on 4
        # outBound of 2 is 1, because 0 is dependent on 2 => to complete 0, 2 needs to complete first
        outBound = {i:0 for i in range(numCourses)}
        if len(prerequisites) > 0:
            for num in prerequisites:
                outBound[num[1]] += 1
        # outbound = [0:0, 1:1, 2:1, 3:1, 4:2]
        q = []
        for i in outBound:
            if outBound[i] == 0: q.append(i)
                
        ans = []
        while q:
            a = q.pop()
            ans.append(a)
            for i in adjacencyList[a]:
                outBound[i] -= 1
                if outBound[i] == 0: q.append(i)
        # Checking if any Loop exits or not. If loop then NO courses can be done => return []. course schedule == False         
        for i in outBound:
            if outBound[i] != 0: return []
            
        return ans[::-1]


