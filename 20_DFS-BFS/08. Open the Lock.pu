# https://leetcode.com/problems/open-the-lock/
# https://youtu.be/Pzg3bCDY87w

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends: 
            return -1
        
        def children(lock):
            arr = []
            for i in range(4):
                cur = int(lock[i])
                arr.append(lock[:i] + str((cur+1)%10) + lock[i+1:])
                arr.append(lock[:i] + str((cur-1)%10) + lock[i+1:])
            return arr
            
        visited = set()
        q = collections.deque()
        q.append(['0000', 0])
            
        while q:
            lock, turns = q.popleft()
            if lock == target: 
                return turns
            for child in children(lock):
                if child not in deadends and child not in visited:
                    visited.add(child)
                    q.append([child, turns+1])
        
        return -1
                    
            
