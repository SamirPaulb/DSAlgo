class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.head = None
    def print_LL(self):
        if self.head is None:
            print("The Node is empty")
        else:
            n = self.head
            while n is not None:
                n = n.ref
                print(n)

LL1 = LinkedList()
LL1.print_LL()
