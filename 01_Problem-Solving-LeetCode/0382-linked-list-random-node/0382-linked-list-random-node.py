class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.arr = []
        cur = head
        self.head = head
        while head:
            self.arr.append(head.val)
            head = head.next
            
    def getRandom(self) -> int:
        return random.choice(self.arr)
