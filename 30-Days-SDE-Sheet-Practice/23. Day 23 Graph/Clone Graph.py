# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# DFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        curNewDict = {}   # key = curNode; value = copy of curNode
        
        def traverse(curNode):
            if not curNode: return
            if curNode not in curNewDict:
                curNewDict[curNode] = Node(curNode.val)
            for nei in curNode.neighbors:
                if nei and nei not in curNewDict: 
                    curNewDict[nei] = Node(nei.val)
                    traverse(nei)  # only calling if nei is not in dictionary. Here we using the curNewDic to track visited nodes also! 
                curNewDict[curNode].neighbors.append(curNewDict[nei])
                
        traverse(node)
        # return copy of the starting node
        return curNewDict[node]
        
    
# BFS
import collections
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        curNewDict = {}   # key = curNode; value = copy of curNode
        
        q = collections.deque()
        q.append(node)
        while q:
            curNode = q.popleft()
            if curNode not in curNewDict: curNewDict[curNode] = Node(curNode.val)
            for nei in curNode.neighbors:
                if nei and nei not in curNewDict: 
                    curNewDict[nei] = Node(nei.val)
                    q.append(nei)  # we are not using any visited set to avoid loop. As we are only appending nei, if nei is not in dictionary. Here we using the curNewDic to track visited nodes also! 
                curNewDict[curNode].neighbors.append(curNewDict[nei])
        # return copy of the starting node
        return curNewDict[node]


# Time for both dfs and bfs is = number of nodes + number of edges
# Time: O(n + e)
# Space: O(n) + o(n)  
# Auxiliary Space: O(n)