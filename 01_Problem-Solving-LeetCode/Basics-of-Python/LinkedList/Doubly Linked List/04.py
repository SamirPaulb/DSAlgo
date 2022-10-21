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

    def insert_only_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("The Linked List is Not Empty")
        
    def add_begin(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.nref = self.head
            self.head.pref  = new_node
            self.head = new_node
    
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n  = n.nref
            n.nref = new_node
            new_node.pref = n

    def add_after(self,data,x):
        new_node = Node(data)
        n = self.head
        if n is None:
            print("DLL is Empty")
        while n is not  None:
            if n.data == x:
                break
            n = n.nref
        if n is None:
            print("Node is Not Present")
        if n.nref is None:
            n.nref = new_node
            new_node.pref = n
        else:
            new_node.nref = n.nref
            n.nref.pref = new_node
            n.nref = new_node
            new_node.pref = n
    
    def add_before(self,data,x):
        new_node = Node(data)
        n = self.head
        if n is None:
            print("DLL is Empty")
        if n.data == x:
            self.head.pref = new_node
            new_node.nref = self.head
            return
        while n.nref is not  None:
            if n.nref.data == x:
                break
            n = n.nref
        if n.nref is None:
            print("Node is Not Present")
        else:
            n.nref.pref = new_node
            new_node.pref = n
            new_node.nref = n.nref
            









DLL = DoublyLL()
DLL.insert_only_empty(10)
DLL.add_begin(29)
DLL.add_begin(40)
DLL.add_begin(50)
DLL.add_end(403)
DLL.add_end(9494838494)
DLL.add_after(5000,29)
DLL.add_before(540,29)




DLL.print_DLL()
DLL.print_DLL_reverse()
