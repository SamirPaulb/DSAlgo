# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/

# Method - 1

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = list(preorder.split(','))
        if preorder[0] == '#':
            return len(preorder) == 1
        
        stack = []  # storing 2 to represent left and right child 
        for i, ch in enumerate(preorder):
            if ch == '#':
                if not stack: return False
                stack[-1] -= 1
                while stack and stack[-1] <= 0:
                    stack.pop()
                    if stack: stack[-1] -= 1
            else:
                if i != 0 and not stack: return False
                stack.append(2)
                
        return True if not stack else False 
    
    
    

# Method - 2
    
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(",")
        n = len(preorder)
        if preorder[0] == '#':
            return n == 1
        stack = [preorder[0]]
        
        for idx in range(1, n):
            if preorder[idx] != '#':
                stack.append(preorder[idx])
            else:
                if not stack:
                    return idx == n - 1
                stack.pop()    
        return False
