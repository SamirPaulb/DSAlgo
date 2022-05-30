# https://leetcode.com/problems/repeated-string-match/
''' 
Python3 program to find minimum number of times 'A' has to be repeated such that 'B' is a substring of it Method to find Minimum number of times 'A' has to be repeated such that 'B' is a substring of it
'''

'''
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        times = ceil(len(b) / len(a))
        
        for i in range(2):
            if b in a * (times + i):
                return times + i
        
        return -1
'''

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        len_a = len(a)
        len_b = len(b)

        for i in range(0, len_a):

            if a[i] == b[0]:
                k = i
                count = 1
                for j in range(0, len_b):

                    # we are reiterating over A again and
                    # again for each value of B
                    # Resetting A pointer back to 0 as B
                    # is not empty yet
                    if k >= len_a:   # or can use k = (k + 1) % m
                        k = 0
                        count = count + 1

                    # Resetting A means count
                    # needs to be increased
                    if a[k] != b[j]:
                        break
                    k = k + 1

                # k is iterating over A
                else:
                    return count
                
        return -1

'''
Time Complexity: O(N * M) 
Auxiliary Space: O(1). 
'''