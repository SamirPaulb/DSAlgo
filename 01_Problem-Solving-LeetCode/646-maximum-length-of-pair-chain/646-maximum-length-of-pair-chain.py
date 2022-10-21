class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x : x[0])
        res = 1
        pre = pairs[0]
        print(pairs)
        for cur in pairs[1:]:
            if cur[0] > pre[1]:
                res += 1
                pre = cur
            else:
                if cur[1] < pre[1]:
                    pre = cur
        
        return res