# https://practice.geeksforgeeks.org/problems/serialize-and-deserialize-a-binary-tree/1

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to serialize a tree and return a list containing nodes of tree.
def serialize(root, A):
    #code here
    def dfs(root):
        if not root: 
            A.append(-1)
            return
        A.append(root.data)
        dfs(root.left)
        dfs(root.right)
    dfs(root)
    return A


#Function to deserialize a list and construct the tree.   
def deSerialize(A):
    #code here
    i = 0
    def dfs():
        nonlocal i
        if i >= len(A): return None
        if A[i] == -1:
            i += 1
            return None
        root = Node(A[i])
        i += 1
        root.left = dfs()
        root.right = dfs()
        return root
    
    return dfs()
    
    
