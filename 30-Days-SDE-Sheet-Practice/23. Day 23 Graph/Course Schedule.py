# https://leetcode.com/problems/course-schedule/
# This problem if a variation of Topological Sort
 
# DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}
        for course in prerequisites:
            adjList[course[0]].append(course[1])
        
        completed = set()
        visited = set()
        
        def canTake(course):
            if course in completed: return True
            if course in visited: return False
            visited.add(course)
            for c in adjList[course]:
                if canTake(c) == False: return False
            completed.add(course)
            return True
        
        for course in adjList:
            if canTake(course) == False: return False
        
        return True

        
        
# BFS
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}
        for course in prerequisites:
            adjList[course[0]].append(course[1])
        # BFS
        # outBound = number of elements dependent on the current element => course to be completed before 
        # eg. for [[0,1], [0,2], [1,3], [1,4], [3,4]] outbound of 4 is 2, because 1 and 3 is dependent on 4
        # outBound of 2 is 1, because 0 is dependent on 2 => to complete 0, 2 needs to complete first
        outbound = {i:0 for i in range(numCourses)}
        for course in prerequisites:
            outbound[course[1]] += 1
        
        q = collections.deque()
        for course in outbound:
            if outbound[course] == 0: q.append(course)
        
        while q:
            course = q.popleft()
            for c in adjList[course]:
                outbound[c] -= 1
                if outbound[c] == 0: q.append(c)
        
        for course in outbound:
            if outbound[course] != 0: return False
        
        return True

# Time for both dfs and bfs is = number of nodes + number of edges
# n = numCourses; e = len(prerequisites)
# Time: O(n + e)
# Space: O(n) + o(n)  
# Auxiliary Space: O(n)
