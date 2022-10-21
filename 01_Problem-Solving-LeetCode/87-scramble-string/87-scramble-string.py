class Solution:
    def isScramble(self, a: str, b: str) -> bool:
        memo = {}
        
        def solve(a, b):
            if len(a) != len(b): return False
            if a == b: return True
            if len(a) <= 1 or len(b) <= 1: return False
            
            key = a + '-' + b
            if key in memo: return memo[key]
            
            ans = False
            for k in range(1, len(a)):
                no_swap = solve(a[:k], b[:k]) and solve(a[k:], b[k:])
                swap = solve(a[:k], b[len(b)-k:]) and solve(a[k:], b[:len(b)-k])
                if no_swap or swap:
                    ans = True
                    break
                    
            memo[key] = ans
            return memo[key]
        
        return solve(a, b)