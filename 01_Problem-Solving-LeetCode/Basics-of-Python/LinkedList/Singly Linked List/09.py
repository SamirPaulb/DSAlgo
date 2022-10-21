class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("The Linked List is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_begin(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node

            
    def add_end(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = self.head
            while new_node.ref is not None:
                new_node = new_node.ref
            new_node.ref = Node(data)
    def add_after(self,data,n):
        tmp = self.head
        i = 0
        while i < n and tmp is not None:
            i = i+1
            tmp = tmp.ref
        
        newNode = Node(data)
        newNode.ref = tmp.ref
        tmp.ref = newNode
        
    



LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_end(2000)
LL1.add_begin(20)
LL1.add_end(300)
LL1.add_after(99,2)
LL1.print_LL()

                











