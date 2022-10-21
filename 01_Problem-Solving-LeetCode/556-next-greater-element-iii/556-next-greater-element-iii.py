class Solution:
    def nextGreaterElement(self, n: int) -> int:
        arr = []
        p = n
        while n:
            arr.append(n%10)
            n = n // 10
        arr.reverse()
        
        l = -1
        r = -1
        
        for i in range(len(arr)-1, 0, -1):
            if arr[i-1] < arr[i]:
                l = i-1
                r = i
                break
        
        if l == -1: return -1
        
        for i in range(r, len(arr)):
            if arr[l] < arr[i]:
                r = i
        
        arr[l], arr[r] = arr[r], arr[l]
        
        l = l+1
        r = len(arr)-1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        
        res = 0
        for i in arr:
            res *= 10
            res += i
        
        return res if res < 2**31 else -1