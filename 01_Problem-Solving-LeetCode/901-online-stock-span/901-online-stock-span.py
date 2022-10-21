class StockSpanner:

    def __init__(self):
        self.stack = []
        self.indx = 0

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        self.indx += 1
        if not self.stack:
            res = self.indx
        else: 
            res = self.indx - self.stack[-1][1]
        self.stack.append([price, self.indx])
        return res


# Time: O(N)
# Space: O(N)