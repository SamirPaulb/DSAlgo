def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.nref
        if n is None:
            print("Given Node is not presnt in Linked List!")
        elif n.nref is None:
            new_node = Node(data)
            n.nref = new_node
            new_node.pref = n
        else:
            new_node = Node(data)
            n.nref.pref = new_node
            new_node.nref = n.nref
            n.nref = new_node
            new_node.pref = n

    def add_before(self,data,x):
        if self.head is None:
            print("Linked List is Empty!")
            return
        if self.head.data == x:
            new_node = Node(data)
            self.head.pref = new_node
            new_node.nref = self.head
            self.head = new_node            
            return
        n = self.head
        while n.nref is not None:
            if x == n.nref.data:
                break
            n = n.nref
        if n.nref is None:
            print("Given Node is not presnt in Linked List!")
        else:
            new_node = Node(data)
            new_node.pref = n
            new_node.nref = n.nref
            n.nref.pref = new_node            
            n.nref = new_node
   