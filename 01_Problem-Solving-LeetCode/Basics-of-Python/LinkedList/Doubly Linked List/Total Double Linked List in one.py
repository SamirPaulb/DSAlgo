#           *****     DOUBLY LINKED LIST IN PYTHON     *****
# Print from forward direction
# Print from backward derection
# Add end
# add begin
# Add after a  node
# add before a node
# Delete at beginning
# Delete at the end 
# Delete element at a given value




class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("The Doubly linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.nref

    def print_ll_reverse(self):
        if self.head is None:
            print("The Doubly linked list is empty")
        else:
            n = self.head 
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data)
                n = n.pref

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
    
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_after_node(self,data,x):
        new_node = Node(data)
        n = self.head
        while n is not None:
            if n.data ==x:
                break
            n = n.nref
        if n is None:
            print("We can't add after None Value, out of bound")
        else:
            if n.nref is None:
                n.nref = new_node
                new_node.pref = n
            else:
                new_node.nref = n.nref
                n.nref.pref = new_node
                n.nref = new_node
                new_node.pref = n

    def add_before_node(self,data,x):
        if self.head is None:
            print("Linked List is Empty!")
            return
        if self.head.data == x:
            new_node = Node(data)
            self.head.pref = new_node
            new_node.nref = self.head
            self.head = new_node            
            return
        n = self.head
        while n.nref is not None:
            if x == n.nref.data:
                break
            n = n.nref
        if n.nref is None:
            print("Given Node is not presnt in Linked List!")
        else:
            new_node = Node(data)
            new_node.pref = n
            new_node.nref = n.nref
            n.nref.pref = new_node            
            n.nref = new_node

    def delete_begine(self):
        if self.head is None:
            print("DLL is empty so can't delete")
            return
        if self.head.nref == None:
            self.head = None
            return
        else:
            self.head = self.head.nref
            self.head.pref = None

    def delete_end(self):
        if self.head is None:
            print("DLL is empty so can't delete")
            return
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

    def delete_by_value(self,x):
        if self.head is None:
            print("DLL is empty so can't delete")
            return
        if self.head.nref is None:
            if self.head.data == x:
                self.head = None
            else:
                print("Given value is not present")
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        else:
            n = self.head
            while n.nref is not None:
                if n.data == x:
                    break
                n = n.nref
            if n.nref is not None:
                n.pref.nref = n.nref
                n.nref = None
                n.pref = None
            else:
                if n.data ==x:
                    n.pref.nref = None
                else:
                    print(f"Can't delete {x} as it is not present")



DLL = DoublyLL()
DLL.add_begin(20)
DLL.add_begin(10)
DLL.add_end(50)
DLL.add_after_node(30,20)
DLL.add_before_node(40,50)
DLL.delete_begine()
DLL.delete_end()
DLL.delete_by_value(100)



DLL.print_ll()
print("----------------------------")
DLL.print_ll_reverse()