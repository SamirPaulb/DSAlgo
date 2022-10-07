# https://leetcode.com/problems/remove-k-digits/
# https://youtu.be/cFabMOnJaq0

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Implement Monotonic Stack (Increasing Order)
        monoStack = []
        for i in num:
            while monoStack and monoStack[-1] > i and k > 0:
                monoStack.pop()
                k -= 1
            monoStack.append(i)
        
        while monoStack and k > 0:
            monoStack.pop()
            k -= 1
        
        res = "".join(monoStack)
        if res == '': return '0'
        res = int(res)  # if num = "10200" => res = 0200
        res = str(res)
        
        return res
