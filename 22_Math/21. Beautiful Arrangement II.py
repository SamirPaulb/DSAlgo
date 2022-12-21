# https://leetcode.com/problems/beautiful-arrangement-ii/

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        numset = {i for i in range(2, n+1)}
        i = 1
        res = [1]
        while k > 1:
            a = i - k
            b = i + k
            if a in numset:
                res.append(a)
                i = a
            else:
                res.append(b)
                i = b
            numset.remove(i)
            k -= 1
        
        return res + list(numset)
    
    
# Time: O(K)
# Space: O(N)
