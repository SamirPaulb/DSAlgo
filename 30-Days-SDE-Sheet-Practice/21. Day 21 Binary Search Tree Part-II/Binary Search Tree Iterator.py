# https://leetcode.com/problems/binary-search-tree-iterator/

'''
Brute Force: 
make a inorder traversal and store all nodes in an array then Time Complexity = O(N); Space = O(N)

class BSTIterator:

    def __init__(self, root):
        self.btree = []
        self.index = -1
        self.inorder(root)

    def next(self) -> int:
        self.index += 1
        return self.btree[self.index]

    def hasNext(self) -> bool:
        return self.index < len(self.btree) - 1
    
    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        self.btree.append(root.val)
        self.inorder(root.right)
'''


# We have to solve in Time = O(H) and Space = O(1) where H is the height of the current calling node

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.getAllLeft(root)

    def next(self) -> int:
        # Get next value in the iterator
        node = self.stack.pop()
        # Append more nodes if there are any on the right
        self.getAllLeft(node.right)
        return node.val
        
    def hasNext(self) -> bool:
        # If the iterator is not empty, there is a NEXT value
        return self.stack
    
    def getAllLeft(self, node:TreeNode) -> None:
        # Add all nodes on the left to the iterator
        while node:
            self.stack.append(node)
            node = node.left
 


