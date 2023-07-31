# https://leetcode.com/problems/lexicographical-numbers/
''' 
Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

Basice idea: think about Trie. we append digits to the specific suffix until we reach the target number.
'''

'''
class Node:
    def __init__(self):
        self.children = {}
        self.val = 0

class Solution:
    def __init__(self):
        self.root = Node()
    
    def addNode(self, s):
        cur = self.root
        for c in s:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.val = int(s)

    def lexicalOrder(self, n: int) -> List[int]:
        for i in range(1, n+1):
            self.addNode(str(i))

        res = []
        def dfs(root):
            for c in root.children:
                node = root.children[c]
                res.append(node.val)
                dfs(node)

        dfs(self.root)
        return res
'''


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # recursively use Trie
        res = []
        # if n < 10:
        #     return list(range(1, n+1))
        for i in range(1, 10):
            res += [i]
            res += self.helper(i, n)
        return res
    
    def helper(self, start, n):
        res = []
        for aux in range(10):
            newStart = start*10+aux
            if newStart > n:
                break
            res += [newStart]
            res += self.helper(newStart, n)
        return res
    
# Time: O(n)
# Space: O(1)
