class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Same as --> Next Greater Element
        
        res = [i for i in range(len(temperatures))] 
        stack = []
        
        for i in range(len(temperatures)-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(i)
        
        for i in range(len(temperatures)):
            res[i] = res[i] - i
        
        return res
    
# Time: O(N)   
# Space: O(N) 