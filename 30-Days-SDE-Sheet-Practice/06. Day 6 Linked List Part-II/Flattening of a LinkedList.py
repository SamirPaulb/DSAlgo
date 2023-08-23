# https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1

''' 
Select 2 bottom directed linklist at a time and use the concept of "21. Merge Two Sorted Lists"
on them. Start traversing from the begining. Assign 'a' linkedList wirh smaller head and
'b' to the larger head. Change main head to a. At the end we will have the sorted Linkedlist with only bottom pointer.

Input:
a     b     c           => take 'a' at smaller head
5 -> 10 -> 19 -> 28
|     |     |     | 
7     20    22   35
|           |     | 
8          50    40
|                 | 
30               45

Output:  5-> 7-> 8- > 10 -> 19-> 20-> 22-> 28-> 30-> 35-> 40-> 45-> 50 bottom pointer

'''


'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
'''

def flatten(head):
    while head.next:
        a, b = head, head.next
        while a:
            if not a.bottom:
                a.bottom = b
                break
            elif not b: break
            elif a.bottom.data > b.data:
                tmp = a.bottom
                a.bottom = b
                b = tmp
            a = a.bottom
        head.next = head.next.next
    
    return head
                

# Time Complexity: O(N*N*M)
# Auxiliary Space: O(1)
