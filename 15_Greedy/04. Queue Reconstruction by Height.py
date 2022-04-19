# https://leetcode.com/problems/queue-reconstruction-by-height/

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x : (-x[0], x[1]))
        res = []
        
        for ch in people:
            res.insert(ch[1], ch)
        
        return res
    
# Time: O(N^2)
# space: O(N)