# https://practice.geeksforgeeks.org/problems/leaves-to-dll/1

def convertToDLL(root):
    #return the head of the DLL and remove those node from the tree as well.
    notLeaves = set()
    
    def isLeaves(root):
        if not root.left and not root.right and root not in notLeaves: return True
        return False
    
    def addToDDL(node):
        nonlocal cur
        cur.right = node
        node.left = cur
        cur = cur.right

    dummy = Node(-1)
    cur = dummy
    
    def dfs(root):
        nonlocal cur
        if not root: return
        dfs(root.left)
        if root.left and isLeaves(root.left):
            node = root.left
            root.left = None
            addToDDL(node)
            notLeaves.add(root)
        if root.right and isLeaves(root.right):
            node = root.right
            root.right = None
            addToDDL(node)
            notLeaves.add(root)
        dfs(root.right)
    
    dfs(root)
    
    res = dummy.right
    dummy.right = None
    res.left = None
    
    return res
            
        
