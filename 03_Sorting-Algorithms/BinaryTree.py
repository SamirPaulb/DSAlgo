class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insertNode(self, data):
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insertNode(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insertNode(data)
        else:
            self.data = data
    
    def printTree(self):
        if self.left: 
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()


root = Node(10)

arr = [7, 12, 15, 20, 30, 1]

for i in arr:
    root.insertNode(i)

root.printTree()