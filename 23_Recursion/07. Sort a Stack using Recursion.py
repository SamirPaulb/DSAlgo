# https://practice.geeksforgeeks.org/problems/sort-a-stack/1#
# Sort a Stack using Recursion without using any loop

class Solution:
    def sorted(self, stack):   # Main Sort Function
        if not stack: 
            return
        tmp = stack.pop()
        self.sorted(stack)
        self.insertInSortedStack(stack, tmp)
        return stack
    
    def insertInSortedStack(self, stack, tmp):  # Helper function to insert element in sorted stack 
        if not stack:
            stack.append(tmp)
            return
        elif tmp >= stack[-1]:
            stack.append(tmp)
            return
        else:
            top = stack.pop()
            self.insertInSortedStack(stack, tmp)
            stack.append(top)
            return
        
# Time Complexity: O(n2)
# Auxiliary Space: O(N)
        
        
        


#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends