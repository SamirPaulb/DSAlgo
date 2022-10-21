class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustOthers = {(i+1):0 for i in range(n)}
        trustedByOthers = {(i+1):0 for i in range(n)}
        
        for a in trust:
            trustOthers[a[0]] += 1
            trustedByOthers[a[1]] += 1
        
        for i in range(1, n+1):
            if trustOthers[i] == 0 and trustedByOthers[i] == n-1:
                return i
        
        return -1