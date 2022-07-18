# https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1
# https://youtu.be/CiiXBvrX-5A

class Solution:
    def celebrity(self, M, n):
        stack = [i for i in range(n)]
        
        while len(stack) > 1:
            a = stack.pop()
            b = stack.pop()
            if M[a][b] == 1: # a knows b; so a can not be celebrety
                stack.append(b)
            else:
                stack.append(a)
        
        if not stack: return -1
        cel = stack[0]
        # As we haven't checked all rows and cols of cel so we are not sure that cel will be the celebrety
        for j in range(n):
            if M[cel][j] == 1: # cel knows others
                return -1  
        for i in range(n):
            if i != cel and M[i][cel] == 0: # someone does not know cel
                return -1
        
        return cel


# Time: O(n)
# Space: O(n)
