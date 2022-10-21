class Node:
    def __init__(self,data):
        self.data = data
        self.ref  = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_LL(self):
        if self.head is None:
            print("Linkedlist is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_end(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
        new_node = Node(data)
        n.ref = new_node

    def add_begin(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node


    def after_node(self,data, x):
        if self.head is None:
            self.head = Node(data)
        else:
            n = self.head
            while self.head is not None:
                n = n.ref
                if n.data ==x:
                    break
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def before_node(self,data,x):
        if self.head is None:
            print("Linked list is Empty")
            
        elif self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node

        n = self.head
        while n.ref is not None:
            if n.ref.data ==x:
                break
            n = n.ref
        print(n.data)  
        if n.ref is None:
            print("No matches found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
        
        
    




LL = LinkedList()
LL.add_begin(10)
LL.add_begin(30)
LL.add_end(500)
LL.add_end(84)
LL.before_node(391,500)
LL.before_node(20301,84000)
LL.after_node(400,10)
LL.after_node(499,400)

LL.print_LL()




