class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
        
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        elif self.key < data:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
            return
        elif self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
            return

    def search(self,data):
        if self.key == data:
            print("Node is Found")
            return
        if self.key < data:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is NOT found")
            return
        if self.key > data:
            if self.lchild:
                delf.lchild.search(data)
            else:
                print("Node is NOT found")
    def preorder(self):
        print(self.key, end=", ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=", ")
        if self.rchild:
            self.rchild.inorder()
    
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end=", ")

    def delete(self,data):
        if self.key is None:
            print("BST is empty")
        if data<self.key:
            self.lchild = self.lchild.delete()

    def delete(self,data):
        if self.key is None:
            print("Tree is Empty!")   
        elif data > self.key:
            if self.rchild:
                self.rchild  = self.rchild.delete(data)
            else:
                print("Node is Not Present ")
        elif data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("Node is not present")
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
                self.key = node.key
                self.rchild = self.rchild.delete(node.key)
            return self
    



    
      
root = BST(10)
ll = [1,2,33,23,12,33,12,456,66, 51]
for i in ll:
    root.insert(i)
print("Preorder")
root.preorder()
'''
print()
print("Inorder")
root.inorder()
print()
print("Postorder")
root.postorder()
'''
print("----------------------")
root.delete(51)
root.preorder()
        