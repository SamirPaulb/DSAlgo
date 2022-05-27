# https://leetcode.com/problems/student-attendance-record-ii/

'''
Recursion with Memoization
We can maintain a cache, i.e, memo dictionary which will store the number of attendance records according 
to the number of absent and consecutive late counts till index i. 

If we ever encounter a number of absences greater than 1 or a number of consecutive late counts greater 
than 2, our answer is zero. If we find the current state is already visited, it means we have encountered 
the same state before so we return it as an answer. Otherwise, we have three cases to explore:

1. Put P at the current index, the consecutive late count will become 0 and the absent count will remain the same.

2. Put L at the current index, the consecutive late count will increase by 1 and the absent count remains the same.

3. Put A at the current index, the consecutive late count becomes 0, and the absent count increases by 1.

When our index reaches up to n, we can return 1 as we have found a valid order.
'''

class Solution:
    def checkRecord(self, n: int) -> int:
        memo = {}
        mod = 10**9 + 7
        
        def solve(i, a, l):
            if a > 1 or l >= 3: 
                return 0

            if i == n:
                return 1

            key = (i, a, l)

            if key in memo:
                return memo[key]

            ans = 0
            ans = (ans%mod + solve(i+1, a, 0)%mod + solve(i+1, a+1, 0)%mod + solve(i+1, a, l+1)%mod)%mod
            
            memo[key] = ans

            return memo[key]
        
        return solve(0, 0, 0)
    
    
# Time Complexity: O(n)
# Space Complexity: O(n*6) ~ O(n)