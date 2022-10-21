class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        while i < len(path):
            cur = path[i]
            i += 1
            if cur == '/':
                while i < len(path) and path[i] == '/':
                    cur += path[i]
                    i += 1
            else:
                while i < len(path) and path[i] != '/':
                    cur += path[i]
                    i += 1
                    
            if cur == '..': 
                if stack: stack.pop()
            elif cur[0] != '/' and cur != '.': 
                stack.append(cur)
        
        res = ''
        for s in stack: res += '/' + s
            
        return res if res else '/'

    
    
    
'''Test Cases:

"/home/"
"/../"
"/home//foo/"
"/a/./b/../../c/"
"/a//b////c/d//././/.."
"/..."
"/..hidden"
"/a/../../b/../c//.//"
'''