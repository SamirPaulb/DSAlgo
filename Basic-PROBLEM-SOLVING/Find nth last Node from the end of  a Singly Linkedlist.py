# Find nth last Node from the end of the Linkedlist

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:

    def __init__(self):
        self.head = None

    def node_from_end(self):
        if self.head is None:
            print("The Linkedlist is Empty!")
        else:
            temp = self.head
            samir = self.head
            for i in range(n-1):
                temp = temp.next
            while temp.next is not None:
                temp = temp.next
                samir = samir.next
            print(f"The {n}th node from the end of the linkedlist is {samir.data}")

    def add_begine(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

n = int(input("Type the value of n to find  nth last element of this Linkedlist:  "))

LL1 = Linkedlist()
LL1.add_begine(15)
LL1.add_begine(14)
LL1.add_begine(13)
LL1.add_begine(12)
LL1.add_begine(11)
LL1.add_begine(10)
LL1.add_begine(9)
LL1.add_begine(8)
LL1.add_begine(7)
LL1.add_begine(6)
LL1.add_begine(5)
LL1.add_begine(4)
LL1.add_begine(3)
LL1.add_begine(2)
LL1.add_begine(1)

print(LL1.node_from_end())


