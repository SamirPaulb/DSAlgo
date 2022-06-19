# https://leetcode.com/problems/is-graph-bipartite/

'''
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that
all the edges are connected across A and B. If there is a edge within A or B then that graph is Not bipartite.
            0
          /   \
         1     2
         |     |
         3-----4
A = {0, 3, 4}; B = {1, 2}    => node 3 and 4 are connected within set A. so not bipartite

1. All acyclic graphs are Bipartite.
2. Cyclic graph of elven length is Bipartite.
3. Acyclic graph of odd lenght is Not Bipartite.

To find cyclic and acyclic we will keep a dictionay with key as node and value as it's colour. 
If current node is seen previously and it's previous colour is different then it is a cyclic graph with Odd lenght.
'''

import collections

class Solution:
    def isBipartite(self, graph):
        seen = {}  # dictionay with key as node and value as it's colour
        
        for node in range(len(graph)):          # graph may have different disjoint components
            if node not in seen:
                q = collections.deque([(node, 1)])
                while q:
                    node, color = q.popleft()
                    
                    if node in seen:            # graph is cyclic
                        if seen[node] == color: # previour color is same as current color
                            continue            # cyclic graph with EVEN length
                        else:                   # previour color diffrent with current color
                            return False        # cyclic graph with ODD length
                    
                    seen[node] = color
                    # store neighbors nodes with opposit color
                    for nei in graph[node]:
                        q.append((nei, color * (-1)))

        return True  
    

# Time = number of nodes + number of edges
# Time: O(n) + O(n)
# Space: O(n) + o(n)  
# Auxiliary Space: O(n)
