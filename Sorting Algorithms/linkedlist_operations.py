class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 
    
    # Print Node method
    def  print_ll(self):
        if self.head == None:
            print("LinkedList is Empty!")
        else:
            tmp = self.head
            while tmp:
                print(tmp.data, end=" --> ")
                tmp = tmp.next
    
    # Add Node at the beginning
    def add_begin(self, data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
            
    # Add after the end Node
    def add_after(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            tmp = self.head
            while tmp.next:
                tmp = tmp.next
            tmp.next = Node(data)

    # Add after a given Node
    def after_a_given_Node(self, x, data):
        if self.head == None:
            self.head = Node(data)
        else:
            tmp = self.head
            while tmp.next:
                if tmp.data == x:
                    break
                tmp = tmp.next
            if tmp.next == None:
                print(f"The Node {x} is not found in the LinkedList!")
            else:
                newNode = Node(data)
                newNode.next = tmp.next
                tmp.next = newNode

    # Add before A given Node
    def add_before_node(self, x, data):
        if self.head == None:
            print(f"The Node {x} is not found!")
        elif self.head.data == x:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
        else:
            tmp = self.head
            while tmp.next:
                if tmp.next.data == x:
                    break
                tmp = tmp.next
            if tmp.next == None:
                print(f"the given Node {x} is not found in the LinkedList")
            else:
                newNode = Node(data)
                newNode.next = tmp.next
                tmp.next = newNode

    # delete Node by Value
    def delete_node_byValue(self, x):
        if self.head is None:
            print("Can Not add as LL is Empty") 
        elif self.head.data == x:
            self.head = self.head.next
        else:
            tmp = self.head
            while tmp.next:
                if tmp.next.data == x:
                    break
                tmp = tmp.next
            if tmp.next == None:
                print("Npde is Not found!")
            else:
                tmp.next = tmp.next.next

    # delete end Node
    def delete_end_node(self):
        if self.head == None:
            print("Empty LinkedList")
        else:
            tmp = self.head
            while tmp.next.next:
                tmp = tmp.next
            tmp.next = None

    # delete node of a given node
    def delete_next_node(self, x):
        if self.head == None:
            print("Can't delete from Empty LinkedList !")
        else:
            tmp = self.head
            while tmp.next:
                if tmp.data == x:
                    break
                tmp = tmp.next 
            if tmp.next == None:
                print(f"The Node {x} is not found in the Linkedlist!")
            else:
                tmp.next = tmp.next.next 
            

LL = LinkedList()

LL.add_begin(50)
LL.add_begin(40)
LL.add_begin(30)
LL.add_begin(20)
LL.add_begin(10)

LL.print_ll()


