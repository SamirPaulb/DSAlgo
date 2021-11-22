class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def addNode(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            currNode = self.head
            while currNode.next:
                currNode = currNode.next
            currNode.next = Node(value)
        return self.head
    
    def mergeSort(self, a, b):
        result = None
        # Base Cases
        if not a: return b
        if not b: return a
        if a.data <= b.data:
            result = a
            result.next = self.mergeSort(a.next, b)
        else:
            result = b
            result.next = self.mergeSort(a, b.next)
        return result
    
    def sortLinkedList(self, head):
        if not head or not head.next: return head
        m = self.findMiddle(head)
        nextToM = m.next
        m.next = None
        leftPart = self.sortLinkedList(head)
        rightPart = self.sortLinkedList(nextToM)
        sortedList = self.mergeSort(leftPart, rightPart)
        return sortedList
    
    def findMiddle(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def printLinkedList(self, head):
        if not head: 
            print("Empty LinkedList !")
            return
        else:
            while head:
                print(head.data)
                head = head.next

LL = LinkedList()
a = [1,4,45,66,8,89,54,0,5,6,75,675,7,56, 70, 259]
for i in a:
    LL.addNode(i)

LL.head = LL.sortLinkedList(LL.head)
LL.printLinkedList(LL.head)




