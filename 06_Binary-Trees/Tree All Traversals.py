class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    res = []
    
    tmp = []
    def inorder(root):
        if not root: return
        inorder(root.left)
        tmp.append(root.data)
        inorder(root.right)
    inorder(root)
    res.append(tmp)
    
    tmp = []
    def preorder(root):
        if not root: return
        tmp.append(root.data)
        preorder(root.left)
        preorder(root.right)
    preorder(root)
    res.append(tmp)
    
    tmp = []
    def postorder(root):
        if not root: return
        postorder(root.left)
        postorder(root.right)
        tmp.append(root.data)
    postorder(root)
    res.append(tmp)
    
    return res