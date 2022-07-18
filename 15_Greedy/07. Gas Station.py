# https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        # Brute-Force Approach
        # Traverse and check
        if sum(gas) < sum(cost): return -1  
        gc = [(gas[i] - cost[i]) for i in range(len(gas))]
        # gc = [-2,-2, -2, 3, 3]
        def check(i, total):
            total += gc[i]
            if i == len(gc)-1: j = 0
            else: j = i+1
            while total >= 0:
                if j == i: return True
                total += gc[j]
                j += 1
                if j == len(gc):
                    j = 0
            return False
        
        for i in range(len(gas)):
            if check(i, 0): return i
        
        # Time: O(N^2)
        # Space: O(N)
        '''
        
        # Best / Optimized Solution => Greedy approach
        if sum(gas) < sum(cost):  # we loop through the path so total gas > total path cost
            return -1
        
        total = 0
        res = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:  # current total is negetive so it can not be the starting. Hope the next index is the starting path. 
                res = i+1
                total = 0
        
        return res
    
# Time: O(N)
# Space: O(1)
