class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val):     # Append elements to the stack such that minimum element stay at peak of stack 
        if not self.stack:
            self.stack.append([val, val])
        else: 
            self.stack.append([val, min(self.stack[-1][1], val)])    # peak[-1][1] stays minimum always

    def getMin(self): 
        return self.stack[-1][1] if self.stack else []


MS = MinStack()

arr = [1, 2, 5, -4, 54, -46, 9]

for val in arr:
    MS.push(val)

print(MS.getMin())  # -46
print(MS.stack)     # [[1, 1], [2, 1], [5, 1], [-4, -4], [54, -4], [-46, -46], [9, -46]]