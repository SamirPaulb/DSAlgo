# https://www.lintcode.com/problem/3678
# https://leetcode.com/problems/remove-interval/description/

class Solution:
  def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
    ans = []

    for a, b in intervals:
      if a >= toBeRemoved[1] or b <= toBeRemoved[0]:
        ans.append([a, b])
      else:  # a < toBeRemoved[1] and b > toBeRemoved[0]
        if a < toBeRemoved[0]:
          ans.append([a, toBeRemoved[0]])
        if b > toBeRemoved[1]:
          ans.append([toBeRemoved[1], b])

    return ans


# Time: O(n)
# Space: O(n)
