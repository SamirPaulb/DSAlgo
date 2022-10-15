# https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num):
        n = len(num)
        for i in range(1, n//2+1):
            for j in range(1, (n-i)//2+1):
                first, second, remaining = num[:i], num[i:i+j], num[i+j:]
                if ((len(first) > 1 and first[0] == '0') or
                    (len(second) > 1 and second[0] == '0')):
                    continue
                while remaining:
                    addFirstSecond = str(int(first) + int(second))
                    if addFirstSecond == remaining: return True
                    elif remaining.startswith(addFirstSecond):
                        first, second, remaining = (second, addFirstSecond,
                                                    remaining[len(addFirstSecond):])
                    else:
                        break
        
        return False
