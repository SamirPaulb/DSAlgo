class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = collections.deque(version1.split("."))
        v2 = collections.deque(version2.split("."))
        
        while v1 or v2:
            v1_val = 0
            v2_val = 0
            if v1: v1_val = int(v1.popleft())
            if v2: v2_val = int(v2.popleft())
            
            if v1_val > v2_val: return 1
            if v1_val < v2_val: return -1
            
        return 0
    
# Time: O(N)  ; as pop from deque is constant time
# Space: O(N) ; for making v1 and v2