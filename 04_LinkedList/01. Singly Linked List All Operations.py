class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
 
# To print the total LinkedList

    def print_LL(self):
        if self.head is None:
            print("The Linkedlist is Empty")
        else:
            tem = self.head
            while tem is not None:
                print(tem.data)
                tem = tem.next

# Add at the beginning

    def add_begin(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

# Add after the End Node

    def add_end(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            tem = self.head
            while tem.next is not None:
                tem = tem.next
            new_node = Node(data)
            tem.next = new_node
            
# Add after a given Node

    def after_node(self,x,data):
        if self.head is None:
            print("Can Not add as LL is Empty")
        else:
            tem = self.head
            while tem.next is not None:
                if tem.data == x:
                    break
                tem = tem.next
            if tem.next is None:
                print(f"Enter data {x} is out of bound!")
            else:
                new_node = Node(data)
                new_node.next = tem.next
                tem.next = new_node  

# Add before a given node

    def before_node(self,x,data):
        if self.head is None:
            print("Can Not add as LL is Empty") 
        else:
            tem = self.head
            while tem.next is not None:
                if tem.next.data == x:
                    break
                tem = tem.next
            if tem.next is None:
                print(f"Enter data {x} is out of bound!!!")
            else:
                new_node = Node(data)
                new_node.next = tem.next
                tem.next = new_node

# Delete by Value of a Nodde

    def delete_by_value(self,x):
        if self.head is None:
            print("Can Not add as LL is Empty") 
        elif self.head.data ==x:
            self.head = self.head.next
        else:
            tem = self.head
            while tem.next is not None:
                if tem.next.data ==x:
                    break
                tem = tem.next
            if tem.next is None:
                print(f"Entered value {x} is Not found!!!!") 
            else:
                tem.next = tem.next.next

# Delete First Node

    def delete_begining(self):
        if self.head is None:
            print("The LL is Empty so can not be deleted!!!!")
        else:
            self.head = self.head.next

# Delete the end node

    def delete_end(self):
        if self.head is None:
            print("The LL is Empty so can not be deleted!!!!")
        else:
            tem = self.head
            while tem.next.next is not None:
                tem = tem.next
            tem.next = None

# Delete next node of a given node

    def delete_next_node(self,x):
        if self.head is None:
            print("The LL is Empty so can not be deleted!!!!")
        else:
            tem = self.head
            while tem.next is not None:
                if tem.data ==x:
                    break
                tem = tem.next
            if tem.next is None:
                print(f"The given value {x} is out of bound!!!!!!!!!!!!!!!!!!!!!!!")
            else:
                tem.next = tem.next.next


    
            
LL = Linkedlist()

LL.add_begin(40)
LL.add_begin(30)
LL.add_begin(20)
LL.add_begin(10)
LL.add_end(50)
LL.add_end(60)
LL.add_end(70)
LL.after_node(400,100)
LL.before_node(310,5000)
LL.delete_by_value(10)
LL.delete_begining()
LL.delete_end()
LL.delete_next_node(330)

LL.print_LL()

