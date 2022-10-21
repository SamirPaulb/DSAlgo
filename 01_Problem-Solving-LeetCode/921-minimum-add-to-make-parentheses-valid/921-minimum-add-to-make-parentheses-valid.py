class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        '''
        # Method - I  ------- Using Stack ------------------
        stack = []
        for i in s:
            if stack and i == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        return len(stack)
        '''
    
        # Method - II  ------- Without Using Stack ------------
        openp = 0; closep = 0
        for i in s:
            if i == '(':
                openp += 1
            else:
                if openp:
                    openp -= 1
                else:
                    closep += 1
        
        return openp + closep