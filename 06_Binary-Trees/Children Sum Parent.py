# https://practice.geeksforgeeks.org/problems/children-sum-parent/1/#
'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        if not root or (not root.left and not root.right): return 1
        else:
            left_data = root.left.data if root.left else 0
            right_data = root.right.data if root.right else 0
            
            if (root.data == left_data + right_data) and self.isSumProperty(root.left) and self.isSumProperty(root.right):
                return 1
            else:
                return 0

# Time : O(N)
# SPace: O(1)
        
