class BST:

    def __init__(self,key):                # Constractor of the class
        self.key = key
        self.lchild = None
        self.rchild = None

# Insert Operation to a Binary Search Tree

    def insert(self, data):
        if self.key is None:
            self.key = data 
            return
        elif self.key == data:
            return
        elif self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
            return
        elif self.key < data:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
            return
    
# Search a node in a binary Search Tree
    
    def search(self, data):
        if self.key is None:
            
