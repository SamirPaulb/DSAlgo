# https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/

'''
Intuition
The number of odd degree node must be even: 0,2,4,...
if odd.size() == 0, return True
if odd.size() == 2, TODO
if odd.size() == 4, TODO
if odd.size() > 4, return false

Explanation
find the adjList where adjList[i] is the neighbour set of node i.
Find out the list of nodes with odd degree.

In case if we have 2 odds:
option1:
we can link them together, if they are not neighbour.
option2:
we can link both them to node i, if node i is not neighbour of either of them.
otherwise return false.

In case if we have 4 odds a,b,c,d
option1: We can link (a,b) and (c,d)
option2: We can link (a,c) and (b,d)
option3: We can link (a,d) and (c,b)
otherwise return false.
'''

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i:set() for i in range(1, n+1)}
        for a, b in edges:
            adjList[a].add(b)
            adjList[b].add(a)
        
        odd = [i for i in adjList if len(adjList[i]) % 2]
        
        def noLink(a, b):
            # return True if a not in adjList[b] else False
            return (a not in adjList[b]) 
                
        if len(odd) == 2:
            a, b = odd
            return any(noLink(a, i) and noLink(b, i) for i in adjList)
        
        if len(odd) == 4:
            a, b, c, d = odd
            return noLink(a, b) and noLink(c, d) or \
                   noLink(a, c) and noLink(b, d) or \
                   noLink(a, d) and noLink(b, c)
        
        return len(odd) == 0
    
    
'''
Complexity

Time: O(edges)
Space: O(edges)
'''
