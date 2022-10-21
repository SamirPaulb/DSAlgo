class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked list is Empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next
       
    def add_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            print("The Linked list is Not Empty")

    

            
LL = LinkedList()
LL.add_empty(10)
LL.add_empty(20)
LL.print_LL()


