class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_end_LL(self):
        if self.head is None:
            print("The Linked list is Empty")
        else:
            n = self.head
            temp = self.head
            for i in range(3):
                n = n.next
            while n is not None:
                temp = temp.next
                n = n.next
            print(f"the 3rd element from the end is: {temp.data}")


    def add_begin(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

LL = LinkedList()
LL.add_begin(100)
LL.add_begin(90)
LL.add_begin(80)
LL.add_begin(70)
LL.add_begin(60)
LL.add_begin(50)
LL.add_begin(40)
LL.add_begin(30)
LL.add_begin(20)
LL.add_begin(10)

LL.print_end_LL()

