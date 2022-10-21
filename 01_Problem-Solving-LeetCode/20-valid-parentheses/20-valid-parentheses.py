class Solution:
    def isValid(self, s: str) -> bool:
        openP = {"(", "{", "["}
        closeP = {")", "}", "]"}
        
        stack = []
        
        for i in s:
            if i in openP or not stack:
                stack.append(i)
            else:
                if ((i == ")" and stack[-1] == "(") or 
                    (i == "}" and stack[-1] == "{") or 
                    (i == "]" and stack[-1] == "[")):
                        stack.pop()
                else:
                    stack.append(i)
        
        return len(stack) == 0
                