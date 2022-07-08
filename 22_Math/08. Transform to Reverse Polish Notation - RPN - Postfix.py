# https://www.spoj.com/problems/ONP/
'''
Input:
3
(a+(b*c))
((a+b)*(z+x))
((a+t)*((b+(a+c))^(c+d)))

Output:
abc*+
ab+zx+*
at+bac++cd+^*
'''

n = int(input(""))  # number of input string
for i in range(n):
    s = input('')   # input Algebraic Expression with Brackets
    stack = []
    for i in s:
        if i == ')':
            tmp = ""
            while stack:
                t = stack.pop()
                if t == "(":
                    break 
                elif t in "+-*/^":
                    tmp += t 
                else:
                    tmp = t + tmp
            stack.append(tmp)
        else:
            stack.append(i)
    print("".join(stack))
    
