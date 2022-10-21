class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def print_LL(self):
        if self.head is None:
            print("The Linked list is Empty ")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    
    def add_begin(self,data):
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
    
    def delete_end(self):
        if self.head is None:
            print("Can not be deletd as empty LL")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

LL = Linkedlist()
LL.add_begin(10)
LL.add_begin(20)
LL.add_begin(30)
LL.delete_end()


LL.print_LL()



