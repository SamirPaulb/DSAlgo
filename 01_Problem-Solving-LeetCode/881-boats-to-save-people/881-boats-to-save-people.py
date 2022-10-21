class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        l = 0
        r = len(people)-1
        while l <= r:
            curSum = people[l] + people[r]
            
            if curSum <= limit:
                res += 1
                l += 1
                r -= 1
            else:
                res += 1
                r -= 1
        
        return res