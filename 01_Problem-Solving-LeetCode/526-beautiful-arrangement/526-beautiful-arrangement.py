class Solution:
    def countArrangement(self, n: int) -> int:
        arr = [(i+1) for i in range(n)]
        self.res = 0
        
        def solve(arr, i):
            if i == n+1:
                self.res += 1
                return
            for j, ch in enumerate(arr):
                if ch % i == 0 or i % ch == 0:
                    solve(arr[:j] + arr[j+1:], i+1)
            
        solve(arr, 1)
        return self.res