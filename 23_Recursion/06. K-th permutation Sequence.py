# https://leetcode.com/problems/permutation-sequence/
# https://www.youtube.com/watch?v=wT7gcXLYoao

''' 
We if we fix one element then there can be (n-1) factorial of permutations starting with that element.
with this concept find the indeces and keep andding and popping elements from arr.
'''
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = [str(i) for i in range(1, n+1)]
        p = math.factorial(n-1)
        res = ''
        k -= 1
        while k > 0:
            i = k // p
            res += arr[i]
            arr.pop(i)
            k %= p
            n -= 1
            p //= n
            
        res += ''.join(arr)
        return res

# Time Complexity = O(N*N) ; we are traversing nums 1 time but POPPING ELEMENT FROM MIDDLE OF ARRAY TAKES O(N) TIME, AS AFTER POPPING ELEMENTS REARRANGE WITH NEW INDEX. 
# Time Complexity = O(N!) # if we consider the time taken by math.factorial function.
# Space Complexity = O(N) ;    for taking arr.