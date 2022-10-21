class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class LinkededList:
    def __init__(self):
        self.head = None
    def print_LL(self):
        if self.head is None:
            print("The Linkedlist is empty")
        else:
            n = self.head
            while self.head is not None:
                n = n.ref
                print(n)
LL1 = LinkededList()
LL1.print_LL()


            


