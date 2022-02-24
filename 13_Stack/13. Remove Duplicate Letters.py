# https://leetcode.com/problems/remove-duplicate-letters/
# Result should be the smallest in lexicographical order among all possible results.

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        visited = set()
        lastIndexDic = {ch:i for i, ch in enumerate(s)}
        stack = []
        
        for i, ch in enumerate(s):
            if ch not in visited:
                while stack and stack[-1] >= ch and lastIndexDic[stack[-1]] > i:
                    visited.remove(stack.pop())
                stack.append(ch)
                visited.add(ch)
        
        return "".join(stack)

# Time Complexity = O(N)
# Space Complexity = O(N)