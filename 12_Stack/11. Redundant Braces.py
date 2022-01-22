# https://www.interviewbit.com/problems/redundant-braces/

class Solution:
	def braces(self, A):
        stack = []

        for ch in A:
            if ch == ")":
                if stack[-1] == "(": return 1  # False  => Redundant Braces
                flag = True   # check if there any arithmetic operation between opened and closed braces
                while stack[-1] != "(":
                    top = stack.pop()
                    if top == '+' or top == '-' or top == '*' or top == '/':
                        flag = False
                stack.pop()  # Poping "("
                if flag == True: return 1   # False 

            else:
                stack.append(ch)
        
        return 0  # True  => NOT Redundant Braces


# https://youtu.be/aMPXhEdpXFA

''' 
Problem Description:
Given a string A denoting an expression. It contains the following operators '+', '-', '*', '/'. Chech whether A has redundant braces or not.
Return 1 if A has redundant braces, else return 0.
Ex.
A = "((a+b))"        => Output = 1 as ((a+b)) has redundant braces so answer will be 1.
A = "(a+(a+b))"      => Output = 0 as (a+(a+b)) doesn't have have any redundant braces so answer will be 0.
A = "(a)"            => Output = 1 as (a) has redundant braces so answer will be 1.
A = "a+b"            => Output = 0 as a+b doesn't have have any redundant braces so answer will be 0.
'''