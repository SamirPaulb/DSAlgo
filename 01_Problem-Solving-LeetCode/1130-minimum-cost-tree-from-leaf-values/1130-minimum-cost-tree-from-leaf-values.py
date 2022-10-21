class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        arr = [float("inf")] + arr + [float("inf")]
        n = len(arr)
        res = 0
        
        while n > 3:
            mini = min(arr)
            i = arr.index(mini)
            if arr[i-1] < arr[i+1]:
                res += arr[i-1] * arr[i]
            else:
                res += arr[i] * arr[i+1]
            
            arr.remove(mini)
            n = len(arr)
        
        return res