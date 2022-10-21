class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        next = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def add_begin(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node

        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def prinr_LL(self):
        if self.head is None:
            print("Empty LL")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next


LL = LinkedList()
LL.add_begin(5)
LL.add_begin(4)
LL.add_begin(3)
LL.add_begin(2)
LL.add_begin(1)
LL.prinr_LL()
LL.reverse()
print("After reverse")
LL.prinr_LL()

