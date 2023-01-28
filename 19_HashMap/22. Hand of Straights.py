# https://leetcode.com/problems/hand-of-straights/

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cnt = collections.Counter(hand)
        i = 0
        sorted_cnt = sorted(cnt)
        while i < len(cnt):
            c = sorted_cnt[i]
            if cnt[c] > 0:
                for j in range(c, c+groupSize):
                    cnt[j] -= 1
                    if cnt[j] < 0: return False
            else:
                i += 1
        return True
      
      
# Time: O(N log(N))
