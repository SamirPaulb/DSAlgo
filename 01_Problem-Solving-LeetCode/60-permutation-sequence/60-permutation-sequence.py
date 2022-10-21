import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = math.factorial(n-1)
        arr = [str(i+1) for i in range(n)]
        res = ""
        k -= 1
        
        while fact >= 1:
            ind = k // fact
            res += arr[ind]
            arr.pop(ind)
            k = k % fact
            n -= 1
            if n == 0: break
            fact = fact // n
        
        res += "".join(arr)
        return res