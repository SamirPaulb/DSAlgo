"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        d = {node : Node(node.val)}
        q = [node]
        
        while q:
            curNode = q.pop(0)
            for nei in curNode.neighbors:
                if nei not in d:
                    d[nei] = Node(nei.val)
                    d[curNode].neighbors.append(d[nei])
                    q.append(nei)
                else:
                    d[curNode].neighbors.append(d[nei])
        
        return d[node]