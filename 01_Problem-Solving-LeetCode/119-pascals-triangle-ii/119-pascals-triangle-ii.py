class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = [1] * (rowIndex+1)
        
        for i in range(2, rowIndex+1):
            for j in range(i-1, 0, -1):
                arr[j] += arr[j-1]
        
        return arr