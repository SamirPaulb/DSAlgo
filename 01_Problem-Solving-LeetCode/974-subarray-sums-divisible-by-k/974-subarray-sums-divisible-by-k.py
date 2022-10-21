class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainderCount = {i:0 for i in range(k)}
        remainderCount[0] = 1
        curRemainder = 0
        res = 0
        
        for i in nums:
            curRemainder += i
            if curRemainder < 0: curRemainder += k
            curRemainder = curRemainder % k
            if remainderCount[curRemainder] >= 1:
                res += remainderCount[curRemainder]
                remainderCount[curRemainder] += 1
            else:
                remainderCount[curRemainder] = 1
                
        return res