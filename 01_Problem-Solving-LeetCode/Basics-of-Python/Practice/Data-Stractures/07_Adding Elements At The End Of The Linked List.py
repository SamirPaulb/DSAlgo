class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class linkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("The linked list is Empty")
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

            n.ref = Node(data)


LL1 = linkedList()
LL1.add_end(100)
LL1.add_end(500)
LL1.add_end(500)
LL1.add_end(500)
LL1.add_end(500)
LL1.print_LL()



