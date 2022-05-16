# https://leetcode.com/problems/rabbits-in-forest/
# https://youtu.be/9mEUIdP4ytw
'''
If answers[i] == v then the current rabbit must be from a group of (v+1) rabits.
if there are more than (v+1) this coloured rabit then there is a another (v+1)
number of rabit of same group.

So find count of same coloured rabits.
calculate no. of groups and extra group possible.
'''

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic = {}
        for i in range(len(answers)):
            if (answers[i] + 1) not in dic:
                dic[answers[i]+1] = 1
            else:
                dic[answers[i]+1] += 1
        
        res = 0
        for key in dic:
            a = dic[key]
            a //= key
            res += key * a
            if dic[key] % key > 0:
                res += key
        
        return res
    
    
# Time: O(N)
# Space: O(N)
