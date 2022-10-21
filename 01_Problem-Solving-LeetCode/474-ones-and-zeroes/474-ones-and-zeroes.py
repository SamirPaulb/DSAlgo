class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}
        
        def dfs(i, m, n):
            if m < 0 or n < 0: return -2**31
            if i >= len(strs): return 0
            
            z = strs[i].count('0')
            o = strs[i].count('1')
            
            if (i, m, n) in memo: return memo[(i, m, n)]
            
            ans = max(1 + dfs(i+1, m-z, n-o), dfs(i+1, m, n))
            memo[(i, m, n)] = ans
            return ans
            
        return dfs(0, m, n)
    
'''
["10","0001","111001","1","0"]
4
3
'''