# https://leetcode.com/problems/online-stock-span/

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        leftmost = 0
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        
        self.stack.append((price, span))
        return span

# Time: O(N)
# Space: O(N)
