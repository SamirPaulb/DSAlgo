# https://leetcode.com/problems/sliding-window-maximum/
# https://youtu.be/CZQGRp93K4k

# from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        q = collections.deque()
        res = []
        # pop, append from deque => O(1)
        # Making a monotonically decreasing deque => first(0th) element will be always largest 
        
        for i, ch in enumerate(nums):
            
            if q and i - q[0] >= k:   # q[0] is more than k distance from the current i
                q.popleft()
                
            while q and ch > nums[q[-1]]:  # pop smaller values from the q
                q.pop()
                
            q.append(i)  
            
            if i >= k-1:       
                res.append(nums[q[0]])  # as q[0] is largest value in that window 
        
        return res

# Time: O(N)
# Space: O(k)    

'''
Deque (Doubly Ended Queue) in Python is implemented using the module “collections“. 
Deque is preferred over a list in the cases where we need quicker append and pop operations 
from both the ends of the container, as deque provides an O(1) time complexity for append and pop operations
as compared to list which provides O(n) time complexity.
'''