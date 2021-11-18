'''
#LeetCode
1221. Split a String in Balanced Strings
Easy

Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".

Example 4:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'

 

Constraints:

    1 <= s.length <= 1000
    s[i] is either 'L' or 'R'.
    s is a balanced string.

Accepted
148,274
Submissions
175,753
Seen this question in a real interview before?
Loop from left to right maintaining a balance variable when it gets an L increase it by one otherwise decrease it by one.
Whenever the balance variable reaches zero then we increase the answer by one.


'''


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        a = 0
        stack = []
        
        stack.append(s[0])
        i = 1
        while i < len(s):
            
            
            if stack[len(stack)-1] != s[i]:
                stack.pop()
            
            if len(stack) !=0:    
                if stack[len(stack)-1] == s[i]:
                    stack.append(s[i])

                
            if len(stack) ==0:
                a = a+1
                i = i+1
                if i<len(s):
                    stack.append(s[i])
            i = i+1
            
        return a
                