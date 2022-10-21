class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x : x[1], reverse = True)
        res = 0
        i = 0
        while i < len(boxTypes):
            if boxTypes[i][0] > truckSize: 
                res += boxTypes[i][1] * truckSize
                break
            else:
                res += boxTypes[i][1] * boxTypes[i][0]
                truckSize -= boxTypes[i][0]
                i += 1
        
        return res