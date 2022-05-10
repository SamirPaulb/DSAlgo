# https://www.interviewbit.com/problems/subarray-with-given-xor/
# https://youtu.be/lO9R5CaGRPY
'''
Use the concept of Largest subarray with 0 sum.
Keep a dictionary to store the current_perfix_xor(cpx). Suppose the current subarray can be devided 
into 2 parts y and k.

<----cpx---->
[4, 2, 2,  6,  4]
<---y--> <-k->

y ^ k = cpx
take ^ on both side(as k^k = 0)
y = cpx ^ k 

if we got y previously in dictionary then increase the res by that count.
'''
class Solution:
    def solve(self, arr, k):
        dic = {}
        cpx = 0
        res = 0

        for i in arr:
            cpx = cpx ^ i

            y = cpx ^ k
            if y in dic: res += dic[y]
            if cpx == k: res += 1

            if cpx in dic: dic[cpx] += 1
            else: dic[cpx] = 1
        
        return res

# Time: O(N)
# Space: O(N)


'''
# Brute Force:
# The brute force solution is to generate all possible subarrays.
# For each generated subarray we get the respective XOR and then check if this XOR is equal to B. 

class Solution:
    def solve(self, arr, k):
        res = 0
        for i in range(len(arr)):
            xor = 0
            for j in range(i, len(arr)):
                xor = xor ^ arr[j]
                if xor == k: res += 1
        
        return res 
# Time Limit Exceeded
# Time: O(N^2)
# Space: O(1)
'''


