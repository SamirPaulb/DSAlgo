class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = 0
        for capa in trips:
            n = max(n, capa[1], capa[2])
            
        dic = {i:0 for i in range(n+1)}
        for car in trips:
            dic[car[1]] += car[0]
            dic[car[2]] -= car[0]
        
        curCapacity = 0
        for i in range(n):
            curCapacity += dic[i]
            if curCapacity > capacity: return False
        
        return True
    
# Time: O(n); where n = max length of path of trips
# Space: O(n); where n = max length of path of trips