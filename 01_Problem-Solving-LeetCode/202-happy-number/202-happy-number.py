class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()        
        while n != 1:
            a = str(n)
            n = 0
            for i in a:
                n += int(i)**2
            if n == 1: return True
            if n in visited: return False
            visited.add(n)
            
        return True