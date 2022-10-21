class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None
class DoublyLL:
    def __init__(self):
        self.head = None

    def print_DLL(self):
        if self.head is None:
            print("The Linked List is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.nref

    def print_DLL_reverse(self):
        if self.head is None:
            print("The Linked List is Empty!")
        else:
            n = self.head
            while n is not None:
                n = n.nref
            while n is not None:
                print(n.data)
                n = n.pref



    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty!")

    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

DLL = DoublyLL()
DLL.insert_empty(10)
DLL.add_begin(29)
DLL.add_begin(40)
DLL.add_begin(50)
DLL.add_end(293)


DLL.print_DLL()
DLL.print_DLL_reverse()