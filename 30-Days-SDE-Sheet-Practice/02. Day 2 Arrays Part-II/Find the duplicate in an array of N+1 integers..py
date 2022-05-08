# https://leetcode.com/problems/find-the-duplicate-number/
# https://www.youtube.com/watch?v=32Ll35mhWg0

'''
Intuition: 
Use the 2 pointers approach of LinkedList Cycle problem. 
Since there is a duplicate number, we can always say that cycle will be formed.

The slow pointer moves by one step and the fast pointer moves by 2 steps and there exists a cycle so the first collision is bound to happen.

Then start a check pointer from 0 and another pointer from current slow's position.
The value where both collide will be the duplicate element.
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Use concept of 142. Linked List Cycle II (find the node where linked list has cycle)
        
        # start hopping from Node
        slow, fast = 0, 0
        # Cycle detection
        # Let slow jumper and fast jumper meet somewhere in the cycle 
        while True:
            # slow jumper hops 1 step, while fast jumper hops two steps forward.
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
        
        # for locating start node of cycle
        check = 0
        while True:
            # Locate the start node of cycle (i.e., the duplicate number)
            slow = nums[slow]
            check = nums[check]
            
            if check == slow:
                break
        
        return check

# Time: O(n)
# Space: O(1)

'''
Let’s assume the distance between the first element and the first collision is a. 
So slow pointer has traveled a distance while fast(since moving 2 steps at a time) 
has traveled 2a distance. For slow and a fast pointer to collide 2a-a=a should be 
multiple of the length of cycle, Now we place a fast pointer to start.
Assume the distance between the start and duplicate to be x. 
So now the distance between slow and duplicate shows also be x, as seen from the diagram,
and so now fast and slow pointer both should move by one step.
'''